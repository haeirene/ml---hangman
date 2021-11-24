const inputPlayer1 = document.getElementsByClassName('input_video')[0];
//const canvasElement = document.querySelector('.output_canvas')[0];
//const canvasCtx = canvasElement.getContext('2d');

function onResults(results) {
	/*canvasCtx.save();
	canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
	canvasCtx.drawImage(
		results.image, 0, 0, canvasElement.width, canvasElement.height);
	if (results.multiHandLandmarks) {
		for (const landmarks of results.multiHandLandmarks) {
		drawConnectors(canvasCtx, landmarks, HAND_CONNECTIONS,
						{color: '#00FF00', lineWidth: 5});
		drawLandmarks(canvasCtx, landmarks, {color: '#FF0000', lineWidth: 2});
		}
	}
	canvasCtx.restore();*/
}

const hands = new Hands({locateFile: (file) => {
	return `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`;
}});
hands.setOptions({
	maxNumHands: 2,
	modelComplexity: 1,
	minDetectionConfidence: 0.5,
	minTrackingConfidence: 0.5
});
hands.onResults(onResults);

//CAMERA
const camera = new Camera(inputPlayer1, {
	onFrame: async () => {
		await hands.send({image: inputPlayer1});
	},
	width: 480,
	height: 480
});
camera.start();