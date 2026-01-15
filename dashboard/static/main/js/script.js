function showTab(tabId, element){
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => tab.classList.remove('active'));

    document.getElementById(tabId).classList.add('active');

    // Highlight active link
    const links = document.querySelectorAll('nav li a');
    links.forEach(link => link.classList.remove('active-link'));
    element.classList.add('active-link');
}
