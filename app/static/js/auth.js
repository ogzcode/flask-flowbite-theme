const authRequest = async (url, data) => {
    return await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });
}


document.addEventListener('alpine:init', () => {
    Alpine.data('auth', () => ({
        email: '',
        password: '',
        username: '',
        loading: false,
        passwordVisible: false,
        togglePasswordVisibility() {
            this.passwordVisible = !this.passwordVisible;
        },
        login() {
            this.loading = true;
            authRequest('/login', {
                email: this.email,
                password: this.password,
            }).then((response) => {
                console.log(response);
            })
                .finally(() => {
                    this.loading = false;
                });
        },
        register() {
            this.loading = true;
            authRequest('/register', {
                email: this.email,
                password: this.password,
                username: this.username,
            }).then((response) => {
                console.log(response);
            })
                .finally(() => {
                    this.loading = false;
                });
        }
    }));
});