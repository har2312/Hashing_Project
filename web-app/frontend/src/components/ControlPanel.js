import React, { useState } from 'react';

function ControlPanel({
  onCreateTable,
  onInsertKey,
  onSearchKey,
  onDeleteKey,
  onResizeTable,
  onClearTable,
  tableState,
  animationSpeed,
  setAnimationSpeed
}) {
  const [size, setSize] = useState('10');
  const [mode, setMode] = useState('chaining');
  const [keyInput, setKeyInput] = useState('');
  const [newSize, setNewSize] = useState('15');

  const handleCreateTable = () => {
    const sizeNum = parseInt(size);
    if (isNaN(sizeNum) || sizeNum < 1 || sizeNum > 100) {
      alert('Table size must be between 1 and 100');
      return;
    }
    onCreateTable(sizeNum, mode);
  };

  const handleInsertKey = () => {
    if (!keyInput.trim()) {
      alert('Please enter a key');
      return;
    }
    
    // Insert single key
    onInsertKey(keyInput.trim());
    setKeyInput('');
  };

  const handleSearchKey = () => {
    if (!keyInput.trim()) {
      alert('Please enter a key to search');
      return;
    }
    onSearchKey(keyInput.trim());
    setKeyInput('');
  };

  const handleDeleteKey = () => {
    if (!keyInput.trim()) {
      alert('Please enter a key to delete');
      return;
    }
    onDeleteKey(keyInput.trim());
    setKeyInput('');
  };

  const handleResize = () => {
    const newSizeNum = parseInt(newSize);
    if (isNaN(newSizeNum) || newSizeNum < 1 || newSizeNum > 100) {
      alert('New size must be between 1 and 100');
      return;
    }
    onResizeTable(newSizeNum);
  };

  return (
    <div className="bg-white rounded-lg shadow-2xl p-1.5">
      {/* Ultra-compact toolbar */}
      <div className="flex flex-wrap items-center gap-1.5">
        <div className="flex items-center gap-0.5">
          <span className="text-gray-600 text-[10px]">Size</span>
          <input type="number" value={size} onChange={(e)=>setSize(e.target.value)} min="1" max="100"
            className="w-14 px-1 py-0.5 text-[10px] border border-gray-300 rounded" />
        </div>
        <div className="flex items-center gap-0.5">
          <span className="text-gray-600 text-[10px]">Mode</span>
          <select value={mode} onChange={(e)=>setMode(e.target.value)}
            className="px-1 py-0.5 text-[10px] border border-gray-300 rounded">
            <option value="chaining">Chaining</option>
            <option value="linear">Linear</option>
            <option value="quadratic">Quadratic</option>
            <option value="double">Double</option>
          </select>
        </div>
        <button onClick={handleCreateTable} className="bg-blue-600 hover:bg-blue-700 text-white text-[10px] font-semibold py-1 px-2 rounded">Create</button>

        <div className="flex items-center gap-1.5 ml-auto">
          <input type="text" value={keyInput} onChange={(e)=>setKeyInput(e.target.value)}
            placeholder="enter key" onKeyPress={(e)=> e.key==='Enter' && handleInsertKey()}
            className="w-52 px-1.5 py-0.5 text-[10px] border border-gray-300 rounded" />
          <button onClick={handleInsertKey} className="bg-green-600 hover:bg-green-700 text-white text-[10px] font-semibold py-1 px-2 rounded">➕ Insert</button>
          <button onClick={handleSearchKey} className="bg-blue-600 hover:bg-blue-700 text-white text-[10px] font-semibold py-1 px-2 rounded">🔍 Search</button>
          <button onClick={handleDeleteKey} className="bg-orange-600 hover:bg-orange-700 text-white text-[10px] font-semibold py-1 px-2 rounded">🗑️ Delete</button>
          <button onClick={onClearTable} className="bg-red-600 hover:bg-red-700 text-white text-[10px] font-semibold py-1 px-2 rounded">Clear</button>
        </div>

        <div className="flex items-center gap-1">
          <span className="text-gray-600 text-[10px]">Speed</span>
          <input type="range" min="200" max="2000" step="100" value={animationSpeed}
            onChange={(e)=>setAnimationSpeed(parseInt(e.target.value))} className="w-28" />
        </div>
        <div className="flex items-center gap-0.5">
          <input type="number" value={newSize} onChange={(e)=>setNewSize(e.target.value)} min="1" max="100"
            placeholder="New" className="w-14 px-1 py-0.5 text-[10px] border border-gray-300 rounded" />
          <button onClick={handleResize} className="bg-purple-600 hover:bg-purple-700 text-white text-[10px] font-semibold py-1 px-2 rounded">Resize</button>
        </div>
      </div>
    </div>
  );
}

export default ControlPanel;
