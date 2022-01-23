/*
OpenCL RandomForestClassifier
classifier_class_name = ObjectClassifier
feature_specification = area mean_max_distance_to_centroid_ratio
num_ground_truth_dimensions = 1
num_classes = 2
num_features = 2
max_depth = 2
num_trees = 10
apoc_version = 0.6.2
*/
__kernel void predict (IMAGE_in0_TYPE in0, IMAGE_in1_TYPE in1, IMAGE_out_TYPE out) {
 sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;
 const int x = get_global_id(0);
 const int y = get_global_id(1);
 const int z = get_global_id(2);
 float i0 = READ_IMAGE(in0, sampler, POS_in0_INSTANCE(x,y,z,0)).x;
 float i1 = READ_IMAGE(in1, sampler, POS_in1_INSTANCE(x,y,z,0)).x;
 float s0=0;
 float s1=0;
if(i0<436.5){
 s0+=6.0;
} else {
 s1+=3.0;
}
if(i1<1.634181022644043){
 if(i1<1.5982544422149658){
  s0+=1.0;
 } else {
  s1+=2.0;
 }
} else {
 if(i1<1.6950984001159668){
  s0+=5.0;
 } else {
  s1+=1.0;
 }
}
if(i1<1.6950984001159668){
 if(i1<1.6420488357543945){
  s0+=1.0;
  s1+=2.0;
 } else {
  s0+=3.0;
 }
} else {
 s1+=3.0;
}
if(i0<488.0){
 s0+=6.0;
} else {
 s1+=3.0;
}
if(i1<1.7233835458755493){
 if(i0<420.0){
  s0+=4.0;
 } else {
  s1+=1.0;
 }
} else {
 s1+=4.0;
}
if(i1<1.6648356914520264){
 if(i1<1.634181022644043){
  s0+=2.0;
  s1+=2.0;
 } else {
  s0+=4.0;
 }
} else {
 s1+=1.0;
}
if(i1<1.6648356914520264){
 if(i1<1.634181022644043){
  s1+=1.0;
 } else {
  s0+=4.0;
 }
} else {
 s1+=4.0;
}
if(i0<345.0){
 s0+=2.0;
} else {
 s1+=7.0;
}
if(i1<1.6648356914520264){
 if(i0<345.0){
  s0+=4.0;
 } else {
  s1+=2.0;
 }
} else {
 s1+=3.0;
}
if(i0<420.0){
 s0+=2.0;
} else {
 s1+=7.0;
}
 float max_s=s0;
 int cls=1;
 if (max_s < s1) {
  max_s = s1;
  cls=2;
 }
 WRITE_IMAGE (out, POS_out_INSTANCE(x,y,z,0), cls);
}
