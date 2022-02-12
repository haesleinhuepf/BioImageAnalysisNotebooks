/*
OpenCL RandomForestClassifier
classifier_class_name = ObjectSegmenter
feature_specification = gaussian_blur=5 sobel_of_gaussian_blur=5
num_ground_truth_dimensions = 2
num_classes = 2
num_features = 2
max_depth = 2
num_trees = 10
positive_class_identifier = 2
apoc_version = 0.6.3
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
if(i0<117.54747009277344){
 s0+=706.0;
} else {
 if(i1<85.72477722167969){
  s1+=378.0;
 } else {
  s0+=14.0;
 }
}
if(i1<38.67491912841797){
 if(i1<14.327082633972168){
  s0+=216.0;
  s1+=10.0;
 } else {
  s0+=258.0;
  s1+=89.0;
 }
} else {
 if(i1<79.76466369628906){
  s0+=203.0;
  s1+=275.0;
 } else {
  s0+=47.0;
 }
}
if(i1<46.786590576171875){
 if(i1<9.822185516357422){
  s0+=179.0;
  s1+=1.0;
 } else {
  s0+=422.0;
  s1+=140.0;
 }
} else {
 if(i1<81.33183288574219){
  s0+=131.0;
  s1+=208.0;
 } else {
  s0+=17.0;
 }
}
if(i0<126.22744750976562){
 if(i1<72.27606201171875){
  s0+=679.0;
  s1+=1.0;
 } else {
  s0+=34.0;
  s1+=5.0;
 }
} else {
 if(i1<85.39649963378906){
  s1+=371.0;
 } else {
  s0+=8.0;
 }
}
if(i1<37.164520263671875){
 if(i0<131.35333251953125){
  s0+=484.0;
 } else {
  s1+=83.0;
 }
} else {
 if(i0<123.6237564086914){
  s0+=234.0;
 } else {
  s0+=10.0;
  s1+=287.0;
 }
}
if(i1<34.945098876953125){
 if(i1<18.311105728149414){
  s0+=281.0;
  s1+=19.0;
 } else {
  s0+=214.0;
  s1+=65.0;
 }
} else {
 if(i1<80.48577117919922){
  s0+=217.0;
  s1+=277.0;
 } else {
  s0+=25.0;
 }
}
if(i1<24.39528465270996){
 if(i1<11.564120292663574){
  s0+=211.0;
  s1+=5.0;
 } else {
  s0+=154.0;
  s1+=32.0;
 }
} else {
 if(i0<123.38143157958984){
  s0+=366.0;
  s1+=3.0;
 } else {
  s0+=16.0;
  s1+=311.0;
 }
}
if(i0<123.38143157958984){
 if(i0<115.80667114257812){
  s0+=710.0;
 } else {
  s0+=5.0;
  s1+=2.0;
 }
} else {
 if(i1<85.868408203125){
  s1+=368.0;
 } else {
  s0+=13.0;
 }
}
if(i1<24.7958984375){
 if(i0<132.14788818359375){
  s0+=372.0;
 } else {
  s1+=42.0;
 }
} else {
 if(i1<52.70560073852539){
  s0+=233.0;
  s1+=133.0;
 } else {
  s0+=138.0;
  s1+=180.0;
 }
}
if(i0<117.7053451538086){
 s0+=689.0;
} else {
 if(i1<86.08059692382812){
  s1+=388.0;
 } else {
  s0+=21.0;
 }
}
 float max_s=s0;
 int cls=1;
 if (max_s < s1) {
  max_s = s1;
  cls=2;
 }
 WRITE_IMAGE (out, POS_out_INSTANCE(x,y,z,0), cls);
}
