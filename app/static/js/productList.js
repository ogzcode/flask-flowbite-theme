document.addEventListener("alpine:init", () => {
    Alpine.data('productList', () => ({
        perPage: 10,
        products: [],
        total: 0,
        currentPage: 1,
        start: 0,
        end: 0,
        search: '',
        sortBy: 'id',
        sortOrder: 'asc',
        headers: [],

        init() {
            this.fetchProduct();
        },
        fetchProduct(page = 1) {
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
                    this.headers = data.headers;
                });
        },

        toggleSort(value) {
            if (this.sortBy === value) {
                this.sortOrder = this.sortOrder === 'asc' ? 'desc' : 'asc';
            } else {
                this.sortBy = value;
                this.sortOrder = 'asc';
            }
            this.fetchProduct();
        },

        clearFilter() {
            this.search = '';
            this.sortBy = 'id';
            this.sortOrder = 'asc';
            this.page = 1;
            this.fetchProduct();
        },
        exportData() {
            showToast('Data exported successfully', 'success');
        },
        formatDate(date) {
            return new Date(date).toLocaleDateString();
        },
    }));
})