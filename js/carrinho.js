function mostrarCarrinho() {
    const resposta = await fetch("http://10.110.134.2.8080/api/get/carrinho")

    if (!resposta.ok) {
        alert("ERRO AO CARREGAR O CARRINHO")
    }
    else {
        const dados = await resposta.json()
        const carrinho = document.getElementById('carrinho')

        carrinho.innerHTML = "";

        for (let dado of dados) {
            let linha = ` <aside class="cart" id="carrinho">
                <label for="toggle-cart" class="close-cart">✕</label>

                <h2>Seu Carrinho</h2>
                <div class="cart-items" id="123">
                <h3>${dado.produto}</h3>
                <img src="${dado.foto}" alt="">
                </div>

                <div class="cart-footer">
                <strong>Total: R$ 0,00</strong>
                <button>Finalizar</button>
                </div>
            
            </aside>
            `
            carrinho.innerHTML += linha
        }
    }
}

mostrarCarrinho();