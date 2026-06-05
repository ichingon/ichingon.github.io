document.addEventListener('DOMContentLoaded', function() {
    const tooltips = document.querySelectorAll('.iching-tooltip');
    
    tooltips.forEach(tooltip => {
        tooltip.addEventListener('mouseenter', function() {
            const tooltipText = this.querySelector('.tooltip-text');
            if (!tooltipText) return;
            
            // Resetear estilos inline previos
            tooltipText.style.left = '';
            tooltipText.style.right = '';
            tooltipText.style.transform = '';
            
            const rect = this.getBoundingClientRect();
            const tooltipWidth = tooltipText.offsetWidth;
            const viewportWidth = window.innerWidth;
            const margin = 10; // Margen mínimo desde los bordes
            
            // Calcular posición ideal (centrada sobre el término)
            let leftPosition = rect.left + (rect.width / 2) - (tooltipWidth / 2);
            
            // Si se sale por la izquierda
            if (leftPosition < margin) {
                leftPosition = margin;
            }
            // Si se sale por la derecha
            else if (leftPosition + tooltipWidth > viewportWidth - margin) {
                leftPosition = viewportWidth - tooltipWidth - margin;
            }
            
            // Aplicar posición calculada
            tooltipText.style.left = leftPosition + 'px';
            tooltipText.style.transform = 'none';
        });
        
        tooltip.addEventListener('mouseleave', function() {
            const tooltipText = this.querySelector('.tooltip-text');
            if (!tooltipText) return;
            
            // Restaurar estilos originales del CSS
            tooltipText.style.left = '';
            tooltipText.style.right = '';
            tooltipText.style.transform = '';
        });
    });
});