/*
OpenCL RandomForestClassifier
classifier_class_name = ObjectClassifier
feature_specification = area mean_max_distance_to_centroid_ratio standard_deviation_intensity
num_ground_truth_dimensions = 1
num_classes = 3
num_features = 3
max_depth = 2
num_trees = 10
apoc_version = 0.6.2
*/
__kernel void predict (IMAGE_in0_TYPE in0, IMAGE_in1_TYPE in1, IMAGE_in2_TYPE in2, IMAGE_out_TYPE out) {
 sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;
 const int x = get_global_id(0);
 const int y = get_global_id(1);
 const int z = get_global_id(2);
 float i0 = READ_IMAGE(in0, sampler, POS_in0_INSTANCE(x,y,z,0)).x;
 float i1 = READ_IMAGE(in1, sampler, POS_in1_INSTANCE(x,y,z,0)).x;
 float i2 = READ_IMAGE(in2, sampler, POS_in2_INSTANCE(x,y,z,0)).x;
 float s0=0;
 float s1=0;
 float s2=0;
if(i2<40.40360641479492){
 if(i0<634.5){
  s2+=6.0;
 } else {
  s1+=2.0;
 }
} else {
 s0+=1.0;
}
if(i0<742.5){
 if(i2<34.70654296875){
  s2+=3.0;
 } else {
  s0+=1.0;
  s1+=1.0;
 }
} else {
 s0+=4.0;
}
if(i0<634.5){
 if(i2<34.597137451171875){
  s2+=3.0;
 } else {
  s0+=1.0;
  s2+=2.0;
 }
} else {
 if(i1<1.8700802326202393){
  s1+=1.0;
 } else {
  s0+=2.0;
 }
}
if(i1<1.6830904483795166){
 s2+=3.0;
} else {
 if(i2<37.08029556274414){
  s0+=2.0;
 } else {
  s0+=1.0;
  s1+=3.0;
 }
}
if(i0<634.5){
 s2+=3.0;
} else {
 if(i2<39.37026596069336){
  s1+=3.0;
 } else {
  s0+=3.0;
 }
}
if(i1<1.764478087425232){
 if(i2<36.76765060424805){
  s2+=3.0;
 } else {
  s0+=1.0;
  s2+=1.0;
 }
} else {
 if(i1<1.8700802326202393){
  s1+=2.0;
 } else {
  s0+=2.0;
 }
}
if(i2<34.70654296875){
 s2+=3.0;
} else {
 if(i1<1.74745774269104){
  s0+=1.0;
  s2+=2.0;
 } else {
  s0+=3.0;
 }
}
if(i1<1.74745774269104){
 s2+=3.0;
} else {
 s0+=6.0;
}
if(i1<1.74745774269104){
 s2+=5.0;
} else {
 s0+=4.0;
}
if(i0<422.5){
 s0+=2.0;
} else {
 if(i0<610.5){
  s2+=4.0;
 } else {
  s0+=2.0;
  s1+=1.0;
 }
}
 float max_s=s0;
 int cls=1;
 if (max_s < s1) {
  max_s = s1;
  cls=2;
 }
 if (max_s < s2) {
  max_s = s2;
  cls=3;
 }
 WRITE_IMAGE (out, POS_out_INSTANCE(x,y,z,0), cls);
}
