__kernel void denoise_bilateral_2d(
    IMAGE_src_TYPE src,
    IMAGE_dst_TYPE dst,
    float sigma_color,
    float sigma_spatial
)
{
    const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;
    
    const int x = get_global_id(0);
    const int y = get_global_id(1);
    const int z = get_global_id(2);
    
    const int width = GET_IMAGE_WIDTH(src);
    const int height = GET_IMAGE_HEIGHT(src);
    const int depth = GET_IMAGE_DEPTH(src);
    
    // Check bounds
    if (x >= width || y >= height || z >= depth) {
        return;
    }
    
    // Get center pixel value
    const float center_value = READ_IMAGE(src, sampler, POS_src_INSTANCE(x, y, z, 0)).x;
    
    // Calculate kernel radius based on spatial sigma (1-sigma rule)
    const int radius = max(5, (int)ceil(1.0f * sigma_spatial));
    
    // Pre-calculate coefficients
    const float spatial_coeff = -0.5f / (sigma_spatial * sigma_spatial);
    const float color_coeff = -0.5f / (sigma_color * sigma_color);
    
    float sum_weights = 0.0f;
    float sum_values = 0.0f;
    
    // Iterate over neighborhood
    for (int dz = -radius; dz <= radius; dz++) {
        int nz = z + dz;
        if (nz < 0 || nz >= depth) continue;
        
        for (int dy = -radius; dy <= radius; dy++) {
            int ny = y + dy;
            if (ny < 0 || ny >= height) continue;
            
            for (int dx = -radius; dx <= radius; dx++) {
                int nx = x + dx;
                if (nx < 0 || nx >= width) continue;
                
                // Get neighbor pixel value
                float neighbor_value = READ_IMAGE(src, sampler, POS_src_INSTANCE(nx, ny, nz, 0)).x;
                
                // Calculate spatial distance squared
                float spatial_dist2 = (float)(dx * dx + dy * dy + dz * dz);
                
                // Calculate color/intensity difference squared
                float color_diff = neighbor_value - center_value;
                float color_dist2 = color_diff * color_diff;
                
                // Calculate bilateral weight
                float spatial_weight = exp(spatial_dist2 * spatial_coeff);
                float color_weight = exp(color_dist2 * color_coeff);
                float weight = spatial_weight * color_weight;
                
                sum_weights += weight;
                sum_values += neighbor_value * weight;
            }
        }
    }
    
    // Normalize and write result
    float result = sum_values / sum_weights;
    WRITE_IMAGE(dst, POS_dst_INSTANCE(x, y, z, 0), CONVERT_dst_PIXEL_TYPE(result));
}