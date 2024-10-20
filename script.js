document.getElementById('nc-form').addEventListener('submit', function(e) {
    e.preventDefault();

    // Captura os dados do formulário
    const description = document.getElementById('description').value;
    const severity = document.getElementById('severity').value;
    const responsible = document.getElementById('responsible').value;
    const status = document.getElementById('status').value;

    // Adiciona a não-conformidade à tabela
    addNonConformity(description, severity, responsible, status);

    // Salva os dados em um arquivo txt (simulação)
    saveToFile(description, severity, responsible, status);

    // Limpa o formulário
    document.getElementById('nc-form').reset();
});

// Função para adicionar uma não-conformidade à tabela
function addNonConformity(description, severity, responsible, status) {
    const tableBody = document.querySelector('#nc-table tbody');
    const row = document.createElement('tr');

    // Adiciona classes para status
    row.classList.add(status === 'Resolvida' ? 'resolved' : 'pending');

    row.innerHTML = `
        <td>${description}</td>
        <td>${severity}</td>
        <td>${responsible}</td>
        <td>${status}</td>
    `;

    tableBody.appendChild(row);

    // Atualiza a porcentagem de aderência
    updateAdherence();
}

// Função para simular o salvamento em um arquivo txt
function saveToFile(description, severity, responsible, status) {
    const data = `Descrição: ${description}\nSeveridade: ${severity}\nResponsável: ${responsible}\nStatus: ${status}\n-------------------\n`;

    // Cria um arquivo .txt e faz o download
    const blob = new Blob([data], { type: 'text/plain' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'nao_conformidade.txt';
    link.click();
}

// Função para calcular a porcentagem de aderência
function updateAdherence() {
    const rows = document.querySelectorAll('#nc-table tbody tr');
    const total = rows.length;
    const resolved = document.querySelectorAll('#nc-table tbody .resolved').length;

    const adherence = (resolved / total) * 100;
    document.getElementById('adherence').innerText = `Aderência: ${adherence.toFixed(2)}%`;
}
