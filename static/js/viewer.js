function loadPDF(pdfPath) {
    const pdfFrame = document.getElementById("pdfFrame");
    pdfFrame.src = `/${pdfPath}`;
}
