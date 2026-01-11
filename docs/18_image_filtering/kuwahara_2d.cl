__kernel void kuwahara_2d(
    IMAGE_src_TYPE src,
    IMAGE_dst_TYPE dst,
    int kernel_size,
    float sigma
)
{
    const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;
    
    const int x = get_global_id(0);
    const int y = get_global_id(1);
    const int z = get_global_id(2);
    
    const int width = GET_IMAGE_WIDTH(src);
    const int height = GET_IMAGE_HEIGHT(src);
    const int depth = GET_IMAGE_DEPTH(src);
    
    if (x >= width || y >= height || z >= depth) {
        return;
    }
    
    // Calculate radius from kernel size
    int radius = kernel_size / 2;
    
    // Pre-calculate Gaussian weights
    float gaussian_norm = 0.0f;
    float weights[256]; // Support up to kernel_size 16 (radius 8)
    int max_offset = min(radius, 8);
    
    for (int dy = -max_offset; dy <= max_offset; dy++) {
        for (int dx = -max_offset; dx <= max_offset; dx++) {
            float dist_sq = (float)(dx * dx + dy * dy);
            int idx = (dy + max_offset) * (2 * max_offset + 1) + (dx + max_offset);
            weights[idx] = exp(-dist_sq / (2.0f * sigma * sigma));
            gaussian_norm += weights[idx];
        }
    }
    
    // Normalize weights
    for (int i = 0; i < (2 * max_offset + 1) * (2 * max_offset + 1); i++) {
        weights[i] /= gaussian_norm;
    }
    
    // Define 4 quadrants: NW, NE, SW, SE
    float mean[4] = {0.0f, 0.0f, 0.0f, 0.0f};
    float variance[4] = {0.0f, 0.0f, 0.0f, 0.0f};
    float weight_sum[4] = {0.0f, 0.0f, 0.0f, 0.0f};
    
    // Calculate mean and variance for each quadrant
    for (int dy = -max_offset; dy <= max_offset; dy++) {
        for (int dx = -max_offset; dx <= max_offset; dx++) {
            int px = x + dx;
            int py = y + dy;
            
            // Clamp coordinates
            px = clamp(px, 0, width - 1);
            py = clamp(py, 0, height - 1);
            
            float val = READ_IMAGE(src, sampler, POS_src_INSTANCE(px, py, z, 0)).x;
            int weight_idx = (dy + max_offset) * (2 * max_offset + 1) + (dx + max_offset);
            float w = weights[weight_idx];
            
            // Determine which quadrant(s) this pixel belongs to
            // 0: NW (dx <= 0, dy <= 0)
            // 1: NE (dx >= 0, dy <= 0)
            // 2: SW (dx <= 0, dy >= 0)
            // 3: SE (dx >= 0, dy >= 0)
            
            if (dx <= 0 && dy <= 0) {
                mean[0] += val * w;
                weight_sum[0] += w;
            }
            if (dx >= 0 && dy <= 0) {
                mean[1] += val * w;
                weight_sum[1] += w;
            }
            if (dx <= 0 && dy >= 0) {
                mean[2] += val * w;
                weight_sum[2] += w;
            }
            if (dx >= 0 && dy >= 0) {
                mean[3] += val * w;
                weight_sum[3] += w;
            }
        }
    }
    
    // Normalize means
    for (int q = 0; q < 4; q++) {
        if (weight_sum[q] > 0.0f) {
            mean[q] /= weight_sum[q];
        }
    }
    
    // Calculate variance for each quadrant
    for (int dy = -max_offset; dy <= max_offset; dy++) {
        for (int dx = -max_offset; dx <= max_offset; dx++) {
            int px = x + dx;
            int py = y + dy;
            
            px = clamp(px, 0, width - 1);
            py = clamp(py, 0, height - 1);
            
            float val = READ_IMAGE(src, sampler, POS_src_INSTANCE(px, py, z, 0)).x;
            int weight_idx = (dy + max_offset) * (2 * max_offset + 1) + (dx + max_offset);
            float w = weights[weight_idx];
            
            if (dx <= 0 && dy <= 0) {
                float diff = val - mean[0];
                variance[0] += diff * diff * w;
            }
            if (dx >= 0 && dy <= 0) {
                float diff = val - mean[1];
                variance[1] += diff * diff * w;
            }
            if (dx <= 0 && dy >= 0) {
                float diff = val - mean[2];
                variance[2] += diff * diff * w;
            }
            if (dx >= 0 && dy >= 0) {
                float diff = val - mean[3];
                variance[3] += diff * diff * w;
            }
        }
    }
    
    // Normalize variances
    for (int q = 0; q < 4; q++) {
        if (weight_sum[q] > 0.0f) {
            variance[q] /= weight_sum[q];
        }
    }
    
    // BLENDING: Calculate weights based on inverse variance
    // Add small epsilon to avoid division by zero
    const float epsilon = 1e-6f;
    float inv_var[4];
    float total_inv_var = 0.0f;
    
    for (int q = 0; q < 4; q++) {
        // Use inverse of variance as weight (lower variance = higher weight)
        inv_var[q] = 1.0f / (variance[q] + epsilon);
        total_inv_var += inv_var[q];
    }
    
    // Normalize to get blending weights
    float blend_weights[4];
    for (int q = 0; q < 4; q++) {
        blend_weights[q] = inv_var[q] / total_inv_var;
    }
    
    // Blend means from all quadrants using the weights
    float result = 0.0f;
    for (int q = 0; q < 4; q++) {
        result += mean[q] * blend_weights[q];
    }
    
    WRITE_IMAGE(dst, POS_dst_INSTANCE(x, y, z, 0), CONVERT_dst_PIXEL_TYPE(result));
}