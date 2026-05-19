document.addEventListener('DOMContentLoaded', () => {

    const clienteBtn = document.getElementById('clienteBtn');

    const maquinaBtn = document.getElementById('maquinaBtn');

    const cadastroBoxTitle = document.getElementById('cadastroBoxTitle');

    const drawerTitle = document.getElementById('drawerTitle');

    const label1 = document.getElementById('label1');

    const label2 = document.getElementById('label2');

    const label3 = document.getElementById('label3');

    const cadastroDrawer = document.getElementById('cadastroDrawer');

    const overlay = document.querySelector('.cadastro-overlay');

    const novoCadastro = document.getElementById('novoCadastro');

    const alterarCadastro = document.getElementById('alterarCadastro');

    const selectExistenteGroup = document.getElementById('selectExistenteGroup');

    const selectLabel = document.getElementById('selectLabel');

    /* OPEN */

    function openDrawer(){

        cadastroDrawer.classList.add('active');

        overlay.classList.add('active');

    }

    /* CLOSE */

    overlay.addEventListener('click', () => {

        cadastroDrawer.classList.remove('active');

        overlay.classList.remove('active');

    });

    /* CLIENTE */

    clienteBtn.addEventListener('click', () => {

        clienteBtn.classList.add('active');

        maquinaBtn.classList.remove('active');

        cadastroBoxTitle.innerText = 'Clientes';

        drawerTitle.innerText = 'Cadastro de Novo Cliente';

        label1.innerText = 'Nome Cliente';

        label2.innerText = 'CNPJ';

        label3.innerText = 'Responsável';

    });

    /* MAQUINA */

    maquinaBtn.addEventListener('click', () => {

        maquinaBtn.classList.add('active');

        clienteBtn.classList.remove('active');

        cadastroBoxTitle.innerText = 'Máquinas';

        drawerTitle.innerText = 'Cadastro de Nova Máquina';

        label1.innerText = 'Nome Máquina';

        label2.innerText = 'Modelo';

        label3.innerText = 'Status';

    });

    /* NOVO */

    novoCadastro.addEventListener('click', () => {

        openDrawer();

        selectExistenteGroup.classList.add('hidden');

    });

    /* ALTERAR */

    alterarCadastro.addEventListener('click', () => {

        openDrawer();

        selectExistenteGroup.classList.remove('hidden');

        if(clienteBtn.classList.contains('active')){

            selectLabel.innerText = 'Selecionar Cliente';

        }else{

            selectLabel.innerText = 'Selecionar Máquina';

        }

    });

});