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
if(i2<22.66911506652832){
 s1+=4.0;
} else {
 if(i0<562.0){
  s2+=5.0;
 } else {
  s0+=3.0;
 }
}
if(i0<517.5){
 if(i2<22.66911506652832){
  s1+=2.0;
 } else {
  s2+=3.0;
 }
} else {
 if(i1<1.7695845365524292){
  s1+=1.0;
 } else {
  s0+=6.0;
 }
}
if(i0<253.0){
 s1+=4.0;
} else {
 if(i2<26.782554626464844){
  s2+=1.0;
 } else {
  s0+=5.0;
  s1+=1.0;
  s2+=1.0;
 }
}
if(i1<1.8197071552276611){
 if(i2<30.380252838134766){
  s1+=3.0;
  s2+=2.0;
 } else {
  s2+=3.0;
 }
} else {
 s0+=4.0;
}
if(i0<253.0){
 s1+=4.0;
} else {
 if(i2<31.362117767333984){
  s0+=4.0;
 } else {
  s2+=4.0;
 }
}
if(i1<1.769775390625){
 if(i2<22.406959533691406){
  s1+=3.0;
 } else {
  s2+=4.0;
 }
} else {
 s0+=5.0;
}
if(i2<27.044710159301758){
 if(i1<1.606772780418396){
  s1+=1.0;
  s2+=3.0;
 } else {
  s1+=2.0;
 }
} else {
 if(i1<1.7695845365524292){
  s1+=2.0;
 } else {
  s0+=4.0;
 }
}
if(i1<1.7695845365524292){
 if(i1<1.491363525390625){
  s1+=1.0;
 } else {
  s1+=2.0;
  s2+=4.0;
 }
} else {
 s0+=5.0;
}
if(i1<1.606772780418396){
 s2+=5.0;
} else {
 if(i2<23.884361267089844){
  s1+=2.0;
 } else {
  s0+=3.0;
  s1+=2.0;
 }
}
if(i0<667.0){
 if(i0<217.0){
  s1+=3.0;
 } else {
  s0+=1.0;
  s1+=2.0;
  s2+=3.0;
 }
} else {
 s0+=3.0;
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
