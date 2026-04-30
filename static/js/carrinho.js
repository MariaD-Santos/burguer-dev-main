async function mostrarCarrinho() {
    try {
        const resposta = await fetch('/carrinho');

        if (resposta.ok) {
            alert("ERRO AO CARREGAR O CARRINHO");
            return;
        }
        else {
            const dados = await resposta.json();

            // Selecionamos o container específico dos itens para não apagar o botão de finalizar
            const containerItens = document.querySelector('.cart-items');
            const displayTotal = document.querySelector('.cart-footer strong');

            containerItens.innerHTML = ""; // Limpa apenas os itens antigos
            let totalAcumulado = 0;

            for (let dado of dados) {
                totalAcumulado += dado.preco;

                let itemHTML = ` 
                <div class="item-no-carrinho">
                    <h3>${dado.nome}</h3>
                    <img src="${dado.imagem}" alt="${dado.nome}" style="width: 50px;">
                    <p>R$ ${dado.preco.toFixed(2)}</p>
                </div>
            `;
                containerItens.innerHTML += itemHTML;
            }
        }


        // Atualiza o total uma única vez ao final do loop
        displayTotal.innerText = `Total: R$ ${totalAcumulado.toFixed(2)}`;

    } catch (erro) {
        console.error("Erro na requisição:", erro);
    }
}

mostrarCarrinho();