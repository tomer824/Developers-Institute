let allBooks = [
	{
		"title" : "Harry Potter",
		"author" : "J.K. Rolling",
		"image" : "https://www.joshuanhook.com/wp-content/uploads/2014/10/harry-potter-2.jpg", 
		"alreadyRead" : true
	},
	{
		"title" : "Murder on the Orient Express",
		"author" : "Agatha Chritstie",
		"image" : "https://images-na.ssl-images-amazon.com/images/I/919flUdn7IL._SL1500_.jpg",
		"alreadyRead" : false
	}
]

let allBooks = [
    {
    "title": "Rich Dad Poor Dad",
    "author": "Robert T. Kiyosaki",
    "image": "https://covers.audiobooks.com/images/covers/full/9781469202617.jpg",
    "alreadyRead": true
},{
    "title": "The Source",
    "author": "James A. Michener",
    "image": "https://images-na.ssl-images-amazon.com/images/I/91SSNqbncwL.jpg",
    "alreadyRead": false
}]
let my_table = document.createElement("TABLE");
let first_row = document.createElement("tr");
my_table.appendChild(first_row);

let head1 = document.createElement("th");
head1.style.paddingRight = '80px';
let text1 = document.createTextNode('Title');
head1.appendChild(text1);
first_row.appendChild(head1);

let head2 = document.createElement("th");
head2.style.paddingRight = '80px';
let text2 = document.createTextNode('Author');
head2.appendChild(text2);
first_row.appendChild(head2);

let head3 = document.createElement("th");
let text3 = document.createTextNode('Image');
head3.appendChild(text3);
first_row.appendChild(head3);

for (let book of allBooks) {
  let book_row = document.createElement('tr');
  my_table.appendChild(book_row);

  let title_col = document.createElement('td');
  book_row.appendChild(title_col);
  title_col.innerHTML = book['title'];

  let author_col = document.createElement('td');
  book_row.appendChild(author_col);
  author_col.innerHTML = book['author'];

  let pic_col = document.createElement('td');
  let image = document.createElement('img');
  image.setAttribute('src', book['image']);
  image.style.width = '100px';
  pic_col.appendChild(image);
  book_row.appendChild(pic_col);

  if (book['alreadyRead'] == true) {
    book_row.style.color = 'red';
  }
}
document.body.appendChild(my_table);
