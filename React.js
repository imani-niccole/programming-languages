//Jael Mackell
//The list in React

import React, { useState } from 'react';

function ListOperations() {
  const [list, setList] = useState([]);

  const handleAddItem = (event) => {
    event.preventDefault();
    const item = event.target.item.value;
    setList([...list, item]);
    event.target.item.value = '';
  };

  const handleRemoveItem = (event) => =[]
    event.preventDefault();
    const item = event.target.item.value;
    setList(list.filter((i) => i !== item));
    event.target.item.value = '';
  };

  const handleSortList = () => {
    const sortedList = [...list].sort();
    setList(sortedList);
  };

  const handleReverseList = () => {
    const reversedList = [...list].reverse();
    setList(reversedList);
  };

  return (
    <div>
      <h2>List Operations</h2>
      <ul>
        {list.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
      <form onSubmit={handleAddItem}>
        <input type="text" name="item" placeholder="Add item" />
        <button type="submit">Add</button>
      </form>
      <form onSubmit={handleRemoveItem}>
        <input type="text" name="item" placeholder="Remove item" />
        <button type="submit">Remove</button>
      </form>
      <button onClick={handleSortList}>Sort</button>
      <button onClick={handleReverseList}>Reverse</button>
      <p>List length: {list.length}</p>
    </div>
  );
}

export default ListOperations;