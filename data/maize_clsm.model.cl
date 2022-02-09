/*
OpenCL RandomForestClassifier
classifier_class_name = ObjectClassifier
feature_specification = area touching_neighbor_count average_distance_of_touching_neighbors average_distance_of_n_nearest_neighbors=1 average_distance_of_n_nearest_neighbors=6 average_distance_of_n_nearest_neighbors=10
num_ground_truth_dimensions = 1
num_classes = 2
num_features = 6
max_depth = 2
num_trees = 10
apoc_version = 0.6.2
*/
__kernel void predict (IMAGE_in0_TYPE in0, IMAGE_in1_TYPE in1, IMAGE_in2_TYPE in2, IMAGE_in3_TYPE in3, IMAGE_in4_TYPE in4, IMAGE_in5_TYPE in5, IMAGE_out_TYPE out) {
 sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;
 const int x = get_global_id(0);
 const int y = get_global_id(1);
 const int z = get_global_id(2);
 float i0 = READ_IMAGE(in0, sampler, POS_in0_INSTANCE(x,y,z,0)).x;
 float i1 = READ_IMAGE(in1, sampler, POS_in1_INSTANCE(x,y,z,0)).x;
 float i2 = READ_IMAGE(in2, sampler, POS_in2_INSTANCE(x,y,z,0)).x;
 float i3 = READ_IMAGE(in3, sampler, POS_in3_INSTANCE(x,y,z,0)).x;
 float i4 = READ_IMAGE(in4, sampler, POS_in4_INSTANCE(x,y,z,0)).x;
 float i5 = READ_IMAGE(in5, sampler, POS_in5_INSTANCE(x,y,z,0)).x;
 float s0=0;
 float s1=0;
if(i2<47.216957092285156){
 s1+=25.0;
} else {
 s0+=8.0;
}
if(i3<23.6112060546875){
 s1+=28.0;
} else {
 s0+=5.0;
}
if(i2<47.216957092285156){
 s1+=29.0;
} else {
 s0+=4.0;
}
if(i4<31.46689224243164){
 s1+=22.0;
} else {
 if(i4<42.573280334472656){
  s0+=2.0;
  s1+=2.0;
 } else {
  s0+=7.0;
 }
}
if(i3<26.3248233795166){
 s1+=25.0;
} else {
 if(i5<45.347225189208984){
  s0+=1.0;
  s1+=1.0;
 } else {
  s0+=6.0;
 }
}
if(i1<9.5){
 s1+=23.0;
} else {
 s0+=10.0;
}
if(i5<49.74626922607422){
 s1+=26.0;
} else {
 s0+=7.0;
}
if(i4<30.005332946777344){
 s1+=22.0;
} else {
 if(i2<47.216957092285156){
  s1+=3.0;
 } else {
  s0+=8.0;
 }
}
if(i2<39.38726043701172){
 s1+=26.0;
} else {
 s0+=7.0;
}
if(i0<733.5){
 s1+=23.0;
} else {
 s0+=10.0;
}
 float max_s=s0;
 int cls=1;
 if (max_s < s1) {
  max_s = s1;
  cls=2;
 }
 WRITE_IMAGE (out, POS_out_INSTANCE(x,y,z,0), cls);
}
