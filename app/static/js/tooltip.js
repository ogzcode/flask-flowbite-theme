document.addEventListener('alpine:init', () => {
    Alpine.directive('tooltip', (el, { expression }, { Alpine }) => {
        let tooltipText = expression || '';
        let tooltipElement;

        el.addEventListener('mouseover', () => {
            if (!tooltipElement) {
                tooltipElement = document.createElement('div');
                tooltipElement.className = 'absolute -top-10 left-1/2 -translate-x-1/2 z-50 p-2 text-xs text-white bg-gray-600 rounded shadow-lg';
                tooltipElement.textContent = tooltipText;
                el.appendChild(tooltipElement);
            }
            tooltipElement.style.display = 'block';
        });

        el.addEventListener('mouseleave', () => {
            if (tooltipElement) {
                tooltipElement.style.display = 'none';
            }
        });
    });
});
