document.addEventListener('DOMContentLoaded', function() {
    const areaPosts = document.getElementById('posts');
    const modal = document.getElementById('modal');
    const areaComentarios = document.getElementById('comentarios');
    const btnClose = modal.querySelector('.btn-close');

    carregarPosts();

    async function carregarPosts() {
        try {
            areaPosts.innerHTML = '<div class="text-center"><div class="spinner-border"></div></div>';
            
            let respPosts = await fetch('https://jsonplaceholder.typicode.com/posts');
            let posts = await respPosts.json();

            let respUsuarios = await fetch('https://jsonplaceholder.typicode.com/users');
            let usuarios = await respUsuarios.json();
            
            areaPosts.innerHTML = '';
            
            for(let i = 0; i < 10; i++) {
                let post = posts[i];
                let usuario = usuarios.find(u => u.id === post.userId);
                if(usuario) {
                    criarPost(post, usuario);
                }
            }
        } catch(erro) {
            areaPosts.innerHTML = `<div class="alert alert-danger">Erro ao carregar posts: ${erro.message}</div>`;
        }
    }

    function criarPost(post, usuario) {
        let postHtml = `
            <article class="post">
                <div class="topo">
                    <div class="foto">
                        <i class="fas fa-user"></i>
                    </div>
                    <div class="info">
                        <div class="nome">${usuario.name}</div>
                        <div class="email">${usuario.email}</div>
                    </div>
                    <div class="data">
                        <i class="fas fa-clock"></i>
                        Agora
                    </div>
                </div>
                <div class="corpo">
                    <h2 class="titulo">${post.title}</h2>
                    <p class="texto">${post.body}</p>
                </div>
                <div class="acoes">
                    <button class="btn" onclick="carregarComentarios(${post.id})">
                        <i class="far fa-comment"></i>
                        <span>Comentários</span>
                    </button>
                </div>
            </article>
        `;

        areaPosts.innerHTML += postHtml;
    }

    window.carregarComentarios = async function(postId) {
        try {
            areaComentarios.innerHTML = '<div class="text-center"><div class="spinner-border"></div></div>';
            
            let resposta = await fetch(`https://jsonplaceholder.typicode.com/comments?postId=${postId}`);
            let comentarios = await resposta.json();
            
            let htmlComentarios = '';
            for(let comentario of comentarios) {
                htmlComentarios += `
                    <div class="coment">
                        <h6>${comentario.name}</h6>
                        <p class="sec">${comentario.email}</p>
                        <p>${comentario.body}</p>
                    </div>
                `;
            }
            
            areaComentarios.innerHTML = htmlComentarios;
            modal.classList.add('show');
            modal.style.display = 'block';
        } catch(erro) {
            areaComentarios.innerHTML = `<div class="alert alert-danger">Erro ao carregar comentários: ${erro.message}</div>`;
        }
    }

    btnClose.addEventListener('click', function() {
        modal.classList.remove('show');
        modal.style.display = 'none';
    });
});
