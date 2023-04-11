let todoList = [];
function addTodo() {
let input = document.getElementById("new-todo-input");
let newTodo = input.value;
if (newTodo === "") {
  return;
}
  todoList.push(newTodo);
  input.value = "";
  updateTodoList();
}
function updateTodoList() {
  let list = document.getElementById("todo-list");
  list.innerHTML = "";
for (let todo of todoList) {
  let li = document.createElement("li");
  li.innerHTML = `${todo} <button class="button__delete-item" onclick="deleteTodo('${todo}')">x</button>`;
  list.appendChild(li);
}
}
function deleteTodo(todo) {
todoList = todoList.filter(item => item !== todo);
updateTodoList();
}


// lấy danh sách các phần tử li trong ul và thêm sự kiện click cho chúng
var listItems = document.querySelectorAll('#myDropdown li');
for (var i = 0; i < listItems.length; i++) {
listItems[i].addEventListener('click', function(event) {
  // thay đổi nội dung của phần tử span có id là parentName khi click vào phần tử li
  var parentName = document.getElementById('parentName');
  parentName.innerHTML = event.target.innerHTML;
});
}

var dropdown = document.getElementById("myDropdown");

function toggleDropdown() {
dropdown.classList.toggle("show");
}

document.getElementById("parentName").addEventListener("click", toggleDropdown);

var dropdownItems = document.querySelectorAll("#myDropdown li");

dropdownItems.forEach(function(item) {
item.addEventListener("click", function() {
  dropdown.classList.remove("show");
});
});

document.addEventListener("click", function(event) {
if (!event.target.closest("#parent")) {
  dropdown.classList.remove("show");
}
});