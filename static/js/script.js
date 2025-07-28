const API_BASE = "http://127.0.0.1:5000";

// ✅ Show Progress Bar for Uploads
function showProgressBar() {
    let progressBar = document.getElementById("progressContainer");
    if (progressBar) {
        progressBar.style.display = "block";
    } else {
        console.error("Progress bar element not found!");
    }
}

// ✅ Fine-Tuning with Live Logs
document.getElementById("fineTuneBtn").addEventListener("click", function () {
    const modelName = document.getElementById("modelSelect").value;
    const datasetPath = "uploads/dataset.csv"; // Assuming dataset is uploaded

    const batchSize = document.getElementById("batchSize").value;
    const numEpochs = document.getElementById("numEpochs").value;
    const learningRate = document.getElementById("learningRate").value;
    const useSpheron = document.getElementById("useSpheron").checked ? "true" : "false";

    const logContainer = document.getElementById("logOutput");
    if (!logContainer) {
        console.error("Log output container not found!");
        return;
    }

    logContainer.innerHTML = "<p>🟡 Starting fine-tuning...</p>"; // Initial message
    document.getElementById("fineTuneStatus").innerText = "Fine-tuning in progress...";

    const eventSource = new EventSource(
        `${API_BASE}/model/fine-tune-stream?model_name=${modelName}&dataset_path=${datasetPath}&batch_size=${batchSize}&epochs=${numEpochs}&learning_rate=${learningRate}&use_spheron=${useSpheron}`
    );

    eventSource.onmessage = function (event) {
        let message = event.data;
        logContainer.innerHTML += `<p>${message}</p>`;
        logContainer.scrollTop = logContainer.scrollHeight; // Auto-scroll

        if (message.includes("DOWNLOAD_LINK:")) {
            let downloadLink = message.split("DOWNLOAD_LINK:")[1].trim();
            document.getElementById("downloadSection").style.display = "block";
            document.getElementById("downloadBtn").setAttribute("data-model-name", modelName);
        }
    };

    eventSource.onerror = function () {
        eventSource.close();
        document.getElementById("fineTuneStatus").innerText = "✅ Fine-tuning completed! Download your model below.";
    };

    eventSource.addEventListener("done", function () {
        eventSource.close();
        document.getElementById("fineTuneStatus").innerText = "❌ Fine-tuning failed!";
    });
});

// ✅ Download Trained Model
function downloadModel() {
    let modelName = document.getElementById("downloadBtn").getAttribute("data-model-name");
    if (!modelName) {
        alert("Model is not ready for download yet!");
        return;
    }

    let downloadUrl = `${API_BASE}/model/download-model/${modelName}-fine-tuned`;
    window.location.href = downloadUrl;
}

// ✅ Evaluate Model
async function evaluateModel() {
    let modelName = document.getElementById("modelSelect").value;
    let response = await fetch(`${API_BASE}/model/evaluate`, {  // Fixed endpoint
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ model_path: `models/${modelName}-fine-tuned` })
    });

    let result = await response.json();
    document.getElementById("evaluationResult").innerText = JSON.stringify(result.metrics, null, 2);
}

// ✅ Upload Dataset with Progress Bar
async function uploadDataset() {
    let fileInput = document.getElementById("datasetFile");
    let file = fileInput.files[0];

    if (!file) {
        alert("Please select a file!");
        return;
    }

    let formData = new FormData();
    formData.append("file", file);

    let progressBar = document.getElementById("progressBar");
    let progressContainer = document.getElementById("progressContainer");
    let uploadStatus = document.getElementById("uploadStatus");

    progressContainer.style.display = "block"; // Show progress bar
    progressBar.style.width = "0%";
    progressBar.innerText = "0%";
    uploadStatus.innerText = "Uploading dataset...";

    let response = await fetch(`${API_BASE}/dataset/upload`, {
        method: "POST",
        body: formData
    });

    let result = await response.json();

    if (response.ok) {
        let progress = 0;
        let interval = setInterval(() => {
            if (progress >= 100) {
                clearInterval(interval);
                progressBar.innerText = "✅ 100%";
                uploadStatus.innerText = "✅ Dataset uploaded successfully! You can proceed to fine-tune the model.";
            } else {
                progress += 10;
                progressBar.style.width = progress + "%";
                progressBar.innerText = progress + "%";
            }
        }, 200); // Smooth increment effect
    } else {
        uploadStatus.innerText = "❌ Upload failed. Try again!";
        progressContainer.style.display = "none"; // Hide progress bar
    }
}
