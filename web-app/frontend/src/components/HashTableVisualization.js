import React, { useEffect, useState } from 'react';

function HashTableVisualization({ tableState, highlightedBucket }) {
  // Calculate row height dynamically so the entire list fits without scrolling
  const [rowHeight, setRowHeight] = useState(18);
  const n = tableState?.size || 10;

  useEffect(() => {
    const compute = () => {
      // Reserve vertical space for header, control bar, toast, margins
      const reserved = 240; // px, approximate total outside this list
      const available = Math.max(200, window.innerHeight - reserved);
      // Panel header inside this component ~34px
      const listAvail = Math.max(120, available - 34);
      const per = Math.floor(listAvail / Math.max(1, n)) - 1; // minus gap
      // Clamp between 8 and 36px to fit up to 100 buckets
      const rh = Math.max(8, Math.min(36, per));
      setRowHeight(rh);
    };
    compute();
    window.addEventListener('resize', compute);
    return () => window.removeEventListener('resize', compute);
  }, [n]);

  if (!tableState) {
    return (
      <div className="bg-white rounded-xl shadow-2xl p-3 h-full flex items-center justify-center">
        <div className="text-center">
          <div className="text-3xl mb-1">🎯</div>
          <h3 className="text-lg font-bold text-gray-800 mb-1">Create a Hash Table to Begin</h3>
          <p className="text-gray-600 text-xs">Use the control panel above to create your first hash table</p>
        </div>
      </div>
    );
  }

  const getModeIcon = () => {
    const icons = { chaining: '🔗', linear: '➡️', quadratic: '📐', double: '🔁' };
    return icons[tableState.mode] || '🔐';
  };

  const getBucketColor = (bucket, index) => {
    if (highlightedBucket === index) return 'bg-yellow-200 border-yellow-500 shadow-lg';
    if (bucket.type === 'empty') return 'bg-white border-gray-300';
    if (bucket.type === 'tombstone') return 'bg-gray-300 border-gray-500';
    return 'bg-blue-100 border-blue-400';
  };

  const renderBucketContents = (bucket) => {
    const contentTextClass = rowHeight <= 12 ? 'text-[8px]' : 'text-[10px]';
    if (bucket.type === 'empty') {
      return <span className={`text-gray-400 ${contentTextClass} font-mono`}>Ø</span>;
    }
    
    if (bucket.type === 'tombstone') {
      return <span className={`text-gray-600 ${contentTextClass} font-mono line-through`}>DEL</span>;
    }

    // Chaining mode - show horizontal linked boxes
    if (tableState.mode === 'chaining' && bucket.contents.length > 0) {
      return (
        <div className="flex items-center gap-1">
          {bucket.contents.map((key, idx) => (
            <React.Fragment key={idx}>
              <div className={`bg-blue-500 text-white px-2 py-1 rounded ${contentTextClass} font-bold border border-blue-600`}>
                {key}
              </div>
              {idx < bucket.contents.length - 1 && (
                <span className={`text-blue-600 font-bold ${contentTextClass}`}>→</span>
              )}
            </React.Fragment>
          ))}
        </div>
      );
    }

    // Single key for open addressing
    return (
      <div className={`bg-green-500 text-white px-3 py-1 rounded ${contentTextClass} font-bold border border-green-600`}>
        {bucket.contents[0]}
      </div>
    );
  };

  return (
    <div className="bg-white rounded-lg shadow-2xl p-2 h-full flex flex-col">
      <div className="flex items-center justify-between mb-1 pb-1 border-b border-gray-200">
        <h2 className="text-xs font-bold text-gray-800">{getModeIcon()} Hash Table</h2>
        <div className="text-[9px] text-gray-600">
          Size: {tableState.size} | Load: {tableState.load_factor.toFixed(2)} | Count: {tableState.count}
        </div>
      </div>
      
      {/* Vertical list of all buckets - fits without scrollbar */}
      <div className="flex-1 overflow-hidden" style={{ height: 'calc(100vh - 240px)' }}>
        <div className="pr-1">
          {tableState.buckets.map((bucket) => (
            <div
              key={bucket.index}
              className="flex items-center gap-1.5 mb-0.5"
              style={{ minHeight: `${rowHeight}px`, height: `${rowHeight}px` }}
            >
              {/* Index label */}
              <div className="flex-shrink-0 w-8 text-right">
                <span className={`${rowHeight <= 12 ? 'text-[8px]' : 'text-[10px]'} font-bold text-purple-700`}>[{bucket.index}]</span>
              </div>
              
              {/* Arrow */}
              <div className={`flex-shrink-0 text-gray-400 ${rowHeight <= 12 ? 'text-[8px]' : 'text-xs'}`}>→</div>
              
              {/* Bucket box */}
              <div
                className={`flex-1 flex items-center px-1.5 rounded border-2 transition-all ${getBucketColor(bucket, bucket.index)}`}
                style={{ minHeight: `${rowHeight}px`, height: `${rowHeight}px` }}
              >
                <div className={`${rowHeight <= 12 ? 'text-[8px]' : ''} w-full flex items-center`}>{renderBucketContents(bucket)}</div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default HashTableVisualization;
