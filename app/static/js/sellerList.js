document.addEventListener("alpine:init", () => {
    Alpine.data('sellerList', () => ({
        perPage: 10,
        sellers: [],
        total: 0,
        currentPage: 1,
        start: 0,
        end: 10,

        init() {
            this.fetchData();
        },
        fetchData(page = 1) {
            if (page < 1) return;
            
            fetch(`/e-commerce/sellers/data`)
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    this.sellers = data.data;
                });
        },
        exportData() {
            showToast('Data exported successfully', 'success');
        }
    }));
})