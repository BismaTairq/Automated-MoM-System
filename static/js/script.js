document.getElementById("uploadForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const form = new FormData(e.target);
  const res = await fetch("/upload", {
    method: "POST",
    body: form
  });
  const data = await res.json();
  document.getElementById("response").innerText = data.message || data.error;
});
