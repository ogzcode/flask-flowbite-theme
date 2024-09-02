document.addEventListener("alpine:init", () => {
    Alpine.data('productList', () => ({
        products: [],
        total: 0,
        currentPage: 1,
        start: 0,
        end: 0,
        search: '',
        sortBy: 'id',
        sortOrder: 'asc',

        init() {
            this.fetchSales();
        },
        fetchSales(page = 1) {
            if (page < 1) return;
            
            fetch(`/e-commerce/product-list/data?page=${page}&search=${this.search}&sort_by=${this.sortBy}&sort_order=${this.sortOrder}`)
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    this.products = data.data;
                    this.total = data.total;
                    this.currentPage = page;
                    this.start = data.from;
                    this.end = data.to;

                });
        },
        
        exportData() {
            showToast('Data exported successfully', 'success');
        },
        formatDate(date) {
            return new Date(date).toLocaleDateString();
        },
    }));
})