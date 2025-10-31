/**
 * Toggles the display of an individual team member's bio
 * @param {string} bioId - The ID of the bio section to show or hide
 */
function toggleBio(bioId) {
    const bio = document.getElementById(bioId);
    // Toggle between showing and hiding the bio section
    if (bio.style.display === "none" || bio.style.display === "") {
        bio.style.display = "block";
    } else {
        bio.style.display = "none";
    }
}

/**
 * Shows the specified section ('bios', 'vision', or 'rules') and hides the others
 * @param {string} sectionId - The ID of the section to display
 */
function showSection(sectionId) {
    const biosSection = document.getElementById("bios");
    const visionSection = document.getElementById("vision");
    const rulesSection = document.getElementById("rules");

    // Hide all sections first
    biosSection.style.display = "none";
    visionSection.style.display = "none";
    rulesSection.style.display = "none";

    // Display the selected section
    if (sectionId === "bios") {
        biosSection.style.display = "flex";
    } else if (sectionId === "vision") {
        visionSection.style.display = "block";
    } else if (sectionId === "rules") {
        rulesSection.style.display = "block";
    }
}