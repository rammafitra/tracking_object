# tracking_object
a basic background subtractor

#info for tracking_object_backgroundsubtractorKNN
The KNN background subtractor, along with its ability to differentiate between objects and shadows, has worked quite well here. All cars have been individually detected; even
though some cars are close to each other, they have not been merged into one detection. For three out of the five cars, the detection rectangles are accurate. For the dark car in the
bottom-left part of the video frame, the background subtractor has failed to fully differentiate the rear of the car from the asphalt. For the white car in the top-center part of
the frame, the background subtractor has failed to fully differentiate the car and its shadow from the white markings on the road. Nonetheless, overall, this is a useful detection result
that could enable us to count the number of cars traveling in each lane.
