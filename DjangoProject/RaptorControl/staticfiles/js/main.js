// Вызов функции API velociraptor для добавления текущих машин в общий список
function fetchDevices() {
    fetch('/fetch-devices/')  // Маршрут функции
        .then(response => {
            if (response.ok) {
                return response.json();  // Получаем JSON-ответ

            } else {
                console.error('Wrong data response:', response.statusText);
                throw new Error('Network response was not ok.');
            }
        })
        .then(data => {
            updateDeviceTable(data.devices);  // Обновляем таблицу с новыми данными
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
}

// Функция для обновления таблицы устройств
function updateDeviceTable(devices) {
    const tableBody = document.getElementById('device-table-body');
    tableBody.innerHTML = ''; // Очищаем текущую таблицу

    devices.forEach((device, index) => {
        const row = `
            <tr>
                <td>${index + 1}</td>
                <td>${device.hostname}</td>
                <td>${device.uptime}</td>
                <td>${device.boot_time}</td>
                <td>${device.procs}</td>
                <td>${device.os}</td>
                <td>${device.platform}</td>
                <td>${device.kernel_version}</td>
                <td>${device.arch}</td>
            </tr>
        `;
        tableBody.insertAdjacentHTML('beforeend', row); // Добавляем новую строку
    });
}

function toggleDevicesList() {
    const devicesList = document.getElementById('devices-list');
    if (devicesList.style.maxHeight) {
        devicesList.style.maxHeight = null; // Закрываем список ОС
    } else {
        devicesList.style.maxHeight = devicesList.scrollHeight + "px"; // Открываем список ОС
    }
}

function toggleDevicesList() {
        const devicesList = document.getElementById('devices-list');
        devicesList.style.maxHeight = devicesList.style.maxHeight ? null : devicesList.scrollHeight + "px";
}

// Вкладка активностей - открытие и закрытие
function toggleActive() {
    
}

function toggleDropdown() {
    const dropdown = document.getElementById('user-dropdown');
    dropdown.style.display = dropdown.style.display === 'none' || dropdown.style.display === '' ? 'block' : 'none';
}

// Закрыть выпадающее меню, если кликнули вне его
window.onclick = function(event) {
    if (!event.target.matches('.user-panel *')) {
        const dropdowns = document.getElementsByClassName("dropdown");
        for (let i = 0; i < dropdowns.length; i++) {
            const openDropdown = dropdowns[i];
            if (openDropdown.style.display === 'block') {
                openDropdown.style.display = 'none';
            }
        }
    }
}
