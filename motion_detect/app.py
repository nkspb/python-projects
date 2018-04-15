import cv2, pandas
from datetime import datetime

# the reference by which we compare if a moving object appeared
first_frame = None
# contains 0 if no motion, 1 - motion detected
status_list = [None, None]
# contains times when object appeared/disappeared in frames
times = []
df = pandas.DataFrame(columns = ["Start", "End"])
# initialize camera with id 0
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    # is moving object in frame
    detect_status = 0
    # convert image to grayscale for accuracy
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # blur the image to make comparisons more accurate
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # set first_frame on the launch of the app
    if first_frame is None:
        first_frame = gray
        # we have nothing to compare it with yet, so just grab new frames
        continue
    
    # build a delta frame with differences between first and current frame
    delta_frame = cv2.absdiff(first_frame, gray)
    # substitute values > than 30 for 255
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    # smooth threshold frame to remove black holes
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
    # find contours
    (_, contours, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # draw contours
    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue
        detect_status = 1
        # create a rectangle
        (x, y, w, h) = cv2.boundingRect(contour)
        # draw a rectangle on the color frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    status_list.append(detect_status)

    # store only changes in status
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Capturing", gray)
    cv2.imshow("Threshold", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        # fix an issue if the user stops the script when 
        # there's no end time for current frame
        if detect_status == 1:
            times.append(datetime.now())
        break

# build a data frame
for i in range(0, len(times), 2):
    df = df.append({"Start" : times[i], "End" : times[i + 1]}, ignore_index = True)

df.to_csv("times.csv")

video.release()
cv2.destroyAllWindows()