open("C:/structure/code/clesperanto_SIMposium/blobs.tif");

// binarization
setAutoThreshold("Otsu dark");
setOption("BlackBackground", true);
run("Convert to Mask");

// Connected component labeling + measurement
run("Analyze Particles...", "  show=[Count Masks] ");

// Result visualization
run("glasbey on dark");

// Save results
saveAs("Tiff", "C:/structure/code/clesperanto_SIMposium/blobs_labels_imagej.tif");
