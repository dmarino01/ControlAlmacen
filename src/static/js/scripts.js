/*!
    * Start Bootstrap - SB Admin v7.0.4 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2021 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    // 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }
});

document.addEventListener("DOMContentLoaded", function () {
    var tableElement = document.querySelector("#datatablesSimple");
    if (tableElement) {
        const dataTable = new simpleDatatables.DataTable(tableElement, {
            labels: {
                placeholder: "Buscar...",
                perPage: "Resultados por página",
                noRows: "No hay datos disponibles",
                info: "Mostrando {start} a {end} de {rows} resultados",
                allRows: "Todos",
                filter: "Filtrar",
                sort: "Ordenar",
            },
            perPage: 25,
            perPageSelect: [10, 25, 50, 100, "Todos"]
        });
    }
});
