const authRequest = async (url, data) => {
    try {
        const res = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (!res.ok) {
            const response = await res.json();
            throw new Error(response.error);
        }

        return await res.json();
    }
    catch (error) {
        throw new Error(error.message);
    }

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
            })
                .then((response) => {
                    console.log(response);
                })
                .catch((error) => {
                    showToast(error.message, 'error');
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
            })
                .then((response) => {
                    console.log(response);
                })
                .catch((error) => {
                    showToast(error.message, 'error');
                })
                .finally(() => {
                    this.loading = false;
                });
        }
    }));
});