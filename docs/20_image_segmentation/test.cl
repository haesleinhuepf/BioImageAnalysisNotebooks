/*
OpenCL RandomForestClassifier
classifier_class_name = ObjectSegmenter
feature_specification = original gaussian_blur=1 gaussian_blur=2 gaussian_blur=3 gaussian_blur=4 gaussian_blur=5 difference_of_gaussian=1 difference_of_gaussian=2 difference_of_gaussian=3 difference_of_gaussian=4 difference_of_gaussian=5 laplace_box_of_gaussian_blur=1 laplace_box_of_gaussian_blur=2 laplace_box_of_gaussian_blur=3 laplace_box_of_gaussian_blur=4 laplace_box_of_gaussian_blur=5
num_ground_truth_dimensions = 2
num_classes = 2
num_features = 16
max_depth = 2
num_trees = 10
positive_class_identifier = 2
apoc_version = 0.6.3
*/
__kernel void predict (IMAGE_in0_TYPE in0, IMAGE_in1_TYPE in1, IMAGE_in2_TYPE in2, IMAGE_in3_TYPE in3, IMAGE_in4_TYPE in4, IMAGE_in5_TYPE in5, IMAGE_in6_TYPE in6, IMAGE_in7_TYPE in7, IMAGE_in8_TYPE in8, IMAGE_in9_TYPE in9, IMAGE_in10_TYPE in10, IMAGE_in11_TYPE in11, IMAGE_in12_TYPE in12, IMAGE_in13_TYPE in13, IMAGE_in14_TYPE in14, IMAGE_in15_TYPE in15, IMAGE_out_TYPE out) {
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
 float i6 = READ_IMAGE(in6, sampler, POS_in6_INSTANCE(x,y,z,0)).x;
 float i7 = READ_IMAGE(in7, sampler, POS_in7_INSTANCE(x,y,z,0)).x;
 float i8 = READ_IMAGE(in8, sampler, POS_in8_INSTANCE(x,y,z,0)).x;
 float i9 = READ_IMAGE(in9, sampler, POS_in9_INSTANCE(x,y,z,0)).x;
 float i10 = READ_IMAGE(in10, sampler, POS_in10_INSTANCE(x,y,z,0)).x;
 float i11 = READ_IMAGE(in11, sampler, POS_in11_INSTANCE(x,y,z,0)).x;
 float i12 = READ_IMAGE(in12, sampler, POS_in12_INSTANCE(x,y,z,0)).x;
 float i13 = READ_IMAGE(in13, sampler, POS_in13_INSTANCE(x,y,z,0)).x;
 float i14 = READ_IMAGE(in14, sampler, POS_in14_INSTANCE(x,y,z,0)).x;
 float i15 = READ_IMAGE(in15, sampler, POS_in15_INSTANCE(x,y,z,0)).x;
 float s0=0;
 float s1=0;
if(i15<0.13614988327026367){
 if(i13<0.04159998893737793){
  s0+=1958.0;
  s1+=184.0;
 } else {
  s0+=33.0;
  s1+=106.0;
 }
} else {
 if(i9<0.7823410034179688){
  s0+=120.0;
  s1+=180.0;
 } else {
  s0+=61.0;
  s1+=1379.0;
 }
}
if(i13<0.04777151346206665){
 if(i9<0.08579444885253906){
  s0+=2091.0;
  s1+=208.0;
 } else {
  s0+=22.0;
  s1+=72.0;
 }
} else {
 if(i14<2.333765983581543){
  s0+=110.0;
  s1+=566.0;
 } else {
  s0+=15.0;
  s1+=937.0;
 }
}
if(i13<0.15357518196105957){
 if(i0<6.5){
  s0+=1454.0;
  s1+=54.0;
 } else {
  s0+=665.0;
  s1+=249.0;
 }
} else {
 if(i9<2.5730972290039062){
  s0+=104.0;
  s1+=594.0;
 } else {
  s0+=23.0;
  s1+=878.0;
 }
}
if(i13<0.04784327745437622){
 if(i15<0.03833198547363281){
  s0+=1963.0;
  s1+=181.0;
 } else {
  s0+=107.0;
  s1+=152.0;
 }
} else {
 if(i5<51.72209548950195){
  s0+=59.0;
  s1+=1283.0;
 } else {
  s0+=71.0;
  s1+=205.0;
 }
}
if(i15<0.05808520317077637){
 if(i13<0.26841259002685547){
  s0+=2030.0;
  s1+=178.0;
 } else {
  s0+=11.0;
  s1+=63.0;
 }
} else {
 if(i9<0.6598081588745117){
  s0+=102.0;
  s1+=178.0;
 } else {
  s0+=74.0;
  s1+=1385.0;
 }
}
if(i1<12.766095161437988){
 if(i1<3.8005433082580566){
  s0+=1175.0;
  s1+=12.0;
 } else {
  s0+=515.0;
  s1+=114.0;
 }
} else {
 if(i8<-0.6997404098510742){
  s0+=377.0;
  s1+=62.0;
 } else {
  s0+=163.0;
  s1+=1603.0;
 }
}
if(i12<0.2564706802368164){
 if(i10<0.5459651947021484){
  s0+=1983.0;
  s1+=197.0;
 } else {
  s0+=54.0;
  s1+=257.0;
 }
} else {
 if(i8<0.42166996002197266){
  s0+=66.0;
  s1+=91.0;
 } else {
  s0+=65.0;
  s1+=1308.0;
 }
}
if(i14<0.03171348571777344){
 if(i11<1.1393601894378662){
  s0+=2020.0;
  s1+=175.0;
 } else {
  s0+=68.0;
  s1+=71.0;
 }
} else {
 if(i8<0.25641536712646484){
  s0+=60.0;
  s1+=119.0;
 } else {
  s0+=82.0;
  s1+=1426.0;
 }
}
if(i8<0.11523914337158203){
 if(i2<7.958839416503906){
  s0+=1251.0;
  s1+=34.0;
 } else {
  s0+=839.0;
  s1+=318.0;
 }
} else {
 if(i5<48.50870895385742){
  s0+=40.0;
  s1+=1194.0;
 } else {
  s0+=87.0;
  s1+=258.0;
 }
}
if(i13<0.05398160219192505){
 if(i10<0.5480070114135742){
  s0+=2065.0;
  s1+=180.0;
 } else {
  s0+=41.0;
  s1+=115.0;
 }
} else {
 if(i15<0.9456872940063477){
  s0+=75.0;
  s1+=245.0;
 } else {
  s0+=42.0;
  s1+=1258.0;
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
