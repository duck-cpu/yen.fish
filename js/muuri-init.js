var grid; // Declare grid in the global scope

// Muuri Initialization
function initMuuri() {
    console.log("Initializing Muuri...");
    grid = new Muuri('.grid', {
        dragEnabled: true,
        dragHandle: '.cardsHeader',
        layoutOnResize: true,
        showDuration: 600,
        showEasing: 'cubic-bezier(0.215, 0.61, 0.355, 1)',
        visibleStyles: {
            opacity: '1',
            transform: 'scale(1.0)'
        },
        hiddenStyles: {
            opacity: '0',
            transform: 'scale(0.5)'
        },
        layout: {
            fillGaps: true,
        }
    });
    console.log("Grid initialized:", grid);
    grid.refreshItems().layout();
    window.addEventListener('load', function () {
        grid.refreshItems().layout();
    });
    window.addEventListener('resize', function () {
        grid.refreshItems().layout();
    });
}

// Function to handle Muuri filtering
function handleMuuriFiltering() {
    document.querySelectorAll('.sort-btn li').forEach(function (button) {
        button.addEventListener('click', function () {
            document.querySelectorAll('.sort-btn li').forEach(function (btn) {
                btn.classList.remove('active');
            });
            this.classList.add('active');

            var className = this.className.split(' ')[0];
            if (className === 'sort00') {
                grid.filter('*');
            } else {
                grid.filter('.' + className);
            }
        });
    });
}

// Initialize Muuri and filtering on all pages
document.addEventListener("DOMContentLoaded", function () {
    initMuuri(); // Call Muuri initialization on all pages
    handleMuuriFiltering(); // Call function to handle Muuri filtering
});
