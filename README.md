<h1>Camera Capture with OpenCV</h1>

<p>This Python script captures real-time video from your webcam using OpenCV, allows you to capture a frame by pressing the <code>q</code> key, converts it to grayscale, and saves it as an image.</p>

<h2>Features</h2>
<ul>
    <li>Capture live video feed from the default webcam.</li>
    <li>Display the live video feed in a window.</li>
    <li>Capture a single frame, convert it to grayscale, and save it as an image file.</li>
    <li>Save the grayscale image as <code>captured_gray_image.jpg</code>.</li>
</ul>

<h2>Requirements</h2>
<p>Before running the script, make sure you have the following installed:</p>
<ul>
    <li>Python 3.x</li>
    <li>OpenCV library for Python</li>
</ul>
<p>You can install the required package with:</p>
<pre><code>pip install opencv-python</code></pre>

<h2>How to Run</h2>
<ol>
    <li>Clone this repository or download the code.</li>
    <pre><code>git clone https://github.com/your-username/repo-name.git
cd repo-name
    </code></pre>
    <li>Run the script using Python:</li>
    <pre><code>python main.py</code></pre>
    <li>The webcam window will open and display the live feed. Press <code>q</code> to capture an image, which will be converted to grayscale and saved as <code>captured_gray_image.jpg</code>.</li>
</ol>

<h2>Code Explanation</h2>
<p>The script follows these steps:</p>
<ol>
    <li><strong>Initialize the Camera:</strong>
        <ul>
            <li><code>cap = cv2.VideoCapture(0)</code> initializes the default camera (0).</li>
        </ul>
    </li>
    <li><strong>Check Camera Connection:</strong>
        <ul>
            <li>The script checks whether the camera has been successfully opened using <code>cap.isOpened()</code>.</li>
        </ul>
    </li>
    <li><strong>Capture Frames in a Loop:</strong>
        <ul>
            <li>The script reads frames from the webcam in a loop using <code>cap.read()</code> and displays them in a window using <code>cv2.imshow()</code>.</li>
        </ul>
    </li>
    <li><strong>Capture Image on Keypress:</strong>
        <ul>
            <li>When the <code>q</code> key is pressed, the current frame is converted to grayscale using <code>cv2.cvtColor()</code>, saved as <code>captured_gray_image.jpg</code>, and displayed.</li>
        </ul>
    </li>
    <li><strong>Release Resources:</strong>
        <ul>
            <li>The camera is released using <code>cap.release()</code>, and all windows are closed using <code>cv2.destroyAllWindows()</code>.</li>
        </ul>
    </li>
</ol>

<h2>Example Output</h2>
<p>When the <code>q</code> key is pressed, an image like this will be saved as <code>captured_gray_image.jpg</code>:</p>
<img src="path/to/your/example-image.jpg" alt="Grayscale Image Example" width="300">

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>
