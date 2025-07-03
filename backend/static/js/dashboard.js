document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("productForm");
  const generateQRBtn = document.getElementById("generateQRBtn");
  const suggestionPanel = document.getElementById("suggestionPanel");
  const qrCodeDiv = document.getElementById("qrCode");

  let boxId = null;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const item = {
      name: document.getElementById("name").value,
      length: parseFloat(document.getElementById("length").value),
      width: parseFloat(document.getElementById("width").value),
      height: parseFloat(document.getElementById("height").value),
      weight: parseFloat(document.getElementById("weight").value),
      fragile: document.getElementById("fragile").checked
    };

    const response = await fetch("/suggest_box", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ items: [item] })
    });

    const data = await response.json();
    boxId = 1; // Simulated ID

    suggestionPanel.innerHTML = `
      <h3>Suggested Box:</h3>
      <p>Type: ${data.box_type}</p>
      <p>Efficiency: ${data.efficiency}%</p>
      <p>CO₂ Saved: ${data.co2_saved}g</p>
    `;

    qrCodeDiv.innerHTML = "";
    renderThreeBox(item.length, item.width, item.height); // 👈 Render 3D box
  });

  generateQRBtn.addEventListener("click", async () => {
    if (!boxId) {
      alert("Please get a suggestion first.");
      return;
    }

    const response = await fetch("/generate_qr", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ box_id: boxId })
    });

    const data = await response.json();
    qrCodeDiv.innerHTML = `<img src="${data.qr_url}" alt="QR Code" />`;
  });
});

function renderThreeBox(length, width, height) {
  const container = document.getElementById("threeContainer");
  container.innerHTML = ""; // Clear previous render

  // Scale down for visibility
  const scale = 0.02;
  const l = length * scale;
  const w = width * scale;
  const h = height * scale;

  // Scene setup
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000);
  const renderer = new THREE.WebGLRenderer();
  renderer.setSize(container.clientWidth, container.clientHeight);
  container.appendChild(renderer.domElement);

  // Box geometry
  const geometry = new THREE.BoxGeometry(l, h, w);
  const material = new THREE.MeshStandardMaterial({ color: 0xdcb35c, roughness: 0.6 });
  const box = new THREE.Mesh(geometry, material);
  scene.add(box);

  // Lighting
  const light = new THREE.DirectionalLight(0xffffff, 1);
  light.position.set(5, 5, 5);
  scene.add(light);

  const ambient = new THREE.AmbientLight(0x404040); // soft light
  scene.add(ambient);

  // Camera position
  camera.position.z = 2;

  // Animate
  function animate() {
    requestAnimationFrame(animate);
    box.rotation.y += 0.01;
    box.rotation.x += 0.005;
    renderer.render(scene, camera);
  }
  animate();
}
