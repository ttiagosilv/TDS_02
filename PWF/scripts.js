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

async function buscarPersonagem() {
    const personagem = document.getElementById('pokemon').value;
    const resultadoDiv = document.getElementById('resultado-pokemon');

    if (!personagem) {
        resultadoDiv.innerHTML = '<p class="error-message">Por favor, digite o nome do personagem</p>';
        return;
    }

    try {
        const response = await fetch(`https://dragonball-api.com/api/characters?name=${encodeURIComponent(personagem)}&limit=1`);
        const data = await response.json();

        if (response.ok && data.items && data.items.length > 0) {
            const char = data.items[0];
            resultadoDiv.innerHTML = `
                <div class="pokemon-card">
                    <img src="${char.image}" alt="${char.name}">
                    <h3>${char.name}</h3>
                    <p>Raça: ${char.race || 'Desconhecida'}</p>
                    <p>Planeta de Origem: ${char.originPlanet || 'Desconhecido'}</p>
                    <p>Status: ${char.status || 'Desconhecido'}</p>
                    <p>Gênero: ${char.gender || 'Desconhecido'}</p>
                    <p>Ki: ${char.ki || 'Desconhecido'}</p>
                    <p>Transformações: ${char.transformations?.length || 0}</p>
                    <p>Afiliações: ${char.affiliation || 'Desconhecida'}</p>
                </div>
            `;
        } else {
            throw new Error('Personagem não encontrado');
        }
    } catch (error) {
        resultadoDiv.innerHTML = `<p class="error-message">Erro: ${error.message}</p>`;
    }
}
