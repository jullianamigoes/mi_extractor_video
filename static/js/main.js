async function procesarVideo() {
    const urlInput = document.getElementById('videoUrl');
    const btnSubmit = document.getElementById('btnSubmit');
    const btnText = document.getElementById('btnText');
    const spinner = document.getElementById('spinner');
    const statusMsg = document.getElementById('statusMessage');

    const urlValue = urlInput.value.trim();

    if (!urlValue) {
        mostrarEstado("Por favor, ingresa un enlace válido.", "error");
        return;
    }

    // Cambiar interfaz a estado de carga
    setLoadingState(true);
    mostrarEstado("Procesando y extrayendo el archivo... Esto puede tardar según la duración del video.", "info");

    try {
        const response = await fetch('/download', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: urlValue })
        });

        if (response.ok) {
            // Recibir el archivo en binario (blob)
            const blob = await response.blob();
            const downloadUrl = window.URL.createObjectURL(blob);
            
            // Generar un número aleatorio de 4 dígitos (entre 1000 y 9999)
            const randomId = Math.floor(1000 + Math.random() * 9000);

            // Crear elemento <a> temporal para iniciar descarga
            const a = document.createElement('a');
            a.href = downloadUrl;
            a.download = `video_${randomId}.mp4`; // Nombre con número aleatorio (ej: video_4821.mp4)
            document.body.appendChild(a);
            a.click();
            a.remove();

            mostrarEstado("¡Descarga iniciada con éxito!", "success");
            urlInput.value = ''; // Limpiar input
        } else {
            const errorData = await response.json();
            mostrarEstado(`Error: ${errorData.error || 'No se pudo procesar el video.'}`, "error");
        }
    } catch (error) {
        mostrarEstado("Error de conexión al comunicarse con el servidor local.", "error");
    } finally {
        setLoadingState(false);
    }
}

function setLoadingState(isLoading) {
    const btnSubmit = document.getElementById('btnSubmit');
    const btnText = document.getElementById('btnText');
    const spinner = document.getElementById('spinner');

    if (isLoading) {
        btnSubmit.disabled = true;
        btnText.textContent = "Procesando...";
        spinner.classList.remove('hidden');
    } else {
        btnSubmit.disabled = false;
        btnText.textContent = "Obtener Video";
        spinner.classList.add('hidden');
    }
}

function mostrarEstado(mensaje, tipo) {
    const statusMsg = document.getElementById('statusMessage');
    statusMsg.textContent = mensaje;
    statusMsg.className = `status-message ${tipo}`;
}