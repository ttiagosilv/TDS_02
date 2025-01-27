async function buscarUsuarioGithub() {
    const usuario = document.getElementById('usuario').value;
    const resultadoDiv = document.getElementById('resultado-github');

    if (!usuario) {
        resultadoDiv.innerHTML = '<p class="error-message">Por favor, digite um nome de usuário</p>';
        return;
    }

    try {
        const response = await fetch(`https://api.github.com/users/${usuario}`);
        const data = await response.json();

        if (response.ok) {
            resultadoDiv.innerHTML = `
                <div class="user-card">
                    <img src="${data.avatar_url}" alt="Avatar do usuário">
                    <h3>${data.name || data.login}</h3>
                    <p>Seguidores: ${data.followers}</p>
                    <p>Repositórios públicos: ${data.public_repos}</p>
                    <p>Localização: ${data.location || 'Não informada'}</p>
                    <a href="${data.html_url}" target="_blank">Ver perfil</a>
                </div>
            `;
        } else {
            throw new Error('Usuário não encontrado');
        }
    } catch (error) {
        resultadoDiv.innerHTML = `<p class="error-message">Erro: ${error.message}</p>`;
    }
}

async function buscarPokemon() {
    const pokemon = document.getElementById('pokemon').value.toLowerCase();
    const resultadoDiv = document.getElementById('resultado-pokemon');

    if (!pokemon) {
        resultadoDiv.innerHTML = '<p class="error-message">Por favor, digite o nome ou número do Pokémon</p>';
        return;
    }

    try {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon}`);
        const data = await response.json();

        if (response.ok) {
            resultadoDiv.innerHTML = `
                <div class="pokemon-card">
                    <img src="${data.sprites.front_default}" alt="${data.name}">
                    <h3>${data.name.charAt(0).toUpperCase() + data.name.slice(1)}</h3>
                    <p>Número: #${data.id}</p>
                    <p>Tipo: ${data.types.map(type => type.type.name).join(', ')}</p>
                    <p>Altura: ${data.height/10}m</p>
                    <p>Peso: ${data.weight/10}kg</p>
                </div>
            `;
        } else {
            throw new Error('Pokémon não encontrado');
        }
    } catch (error) {
        resultadoDiv.innerHTML = `<p class="error-message">Erro: ${error.message}</p>`;
    }
}
