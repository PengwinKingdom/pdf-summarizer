const pdfFileInput = document.getElementById("pdfFile");
const uploadBtn = document.getElementById("uploadBtn");
const statusMessage = document.getElementById("statusMessage");
const summaryText = document.getElementById("summaryText");
const keyPointsList = document.getElementById("keyPointsList");

uploadBtn.addEventListener("click", async () => {
  const file = pdfFileInput.files[0];

  if (!file) {
    statusMessage.textContent = "Please select a PDF file first.";
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  statusMessage.textContent = "Processing PDF...";
  summaryText.textContent = "Loading summary...";
  keyPointsList.innerHTML = "<li>Loading key points...</li>";

  try {
    const response = await fetch("http://127.0.0.1:8000/upload-pdf", {
      method: "POST",
      body: formData
    });

    const data = await response.json();

    if (!response.ok) {
      statusMessage.textContent = data.error || "Something went wrong.";
      summaryText.textContent = "No summary available.";
      keyPointsList.innerHTML = "<li>No key points available.</li>";
      return;
    }

    statusMessage.textContent = "PDF processed successfully.";
    summaryText.textContent = data.summary || "No summary available.";

    keyPointsList.innerHTML = "";

    if (data.key_points && data.key_points.length > 0) {
      data.key_points.forEach((point) => {
        const li = document.createElement("li");
        li.textContent = point;
        keyPointsList.appendChild(li);
      });
    } else {
      keyPointsList.innerHTML = "<li>No key points available.</li>";
    }

  } catch (error) {
    statusMessage.textContent = "Error connecting to the backend.";
    summaryText.textContent = "No summary available.";
    keyPointsList.innerHTML = "<li>No key points available.</li>";
    console.error(error);
  }
});