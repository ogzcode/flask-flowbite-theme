document.addEventListener('DOMContentLoaded', function () {
    var options = {
        title: {
            text: 'User Activity',
            align: 'left',
            style: {
                fontSize: '16px',
                color: '#4b5563',
                fontWeight: '600'
            }
        },
        chart: {
            type: 'bar',
            height: 320,
            toolbar: {
                show: false
            }
        },
        series: [{
            name: 'User Activity',
            data: [30, 40, 75, 50, 49, 60, 30]
        }],
        xaxis: {
            categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        }
    };

    var chart = new ApexCharts(document.querySelector("#user-activity"), options);

    chart.render();
});

document.addEventListener("alpine:init", () => {
    Alpine.data('dashboard', () => ({
        sales: [],
        total: 0,
        currentPage: 1,
        perPage: 10,
        start: 0,
        end: 0,

        init() {
            this.fetchSales();
        },
        fetchSales(page = 1) {
            if (page < 1) return;
            
            fetch(`/api/sales-table?page=${page}&per_page=${this.perPage}`)
                .then(response => response.json())
                .then(data => {
                    this.sales = data.data;
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
