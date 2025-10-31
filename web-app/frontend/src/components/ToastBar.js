import React, { useEffect, useState } from 'react';

function ToastBar({ message, variant = 'info', autoHide = false, hideAfter = 3000 }) {
  const [visible, setVisible] = useState(Boolean(message));

  useEffect(() => {
    if (message) {
      setVisible(true);
      if (autoHide) {
        const t = setTimeout(() => setVisible(false), hideAfter);
        return () => clearTimeout(t);
      }
    } else {
      setVisible(false);
    }
  }, [message, autoHide, hideAfter]);

  if (!visible) return null;

  const colorMap = {
    info: 'bg-blue-400',
    success: 'bg-green-400',
    warn: 'bg-yellow-400',
    error: 'bg-red-400',
  };

  const dot = colorMap[variant] || colorMap.info;

  return (
    <div className="mt-2">
      <div className="w-full bg-gray-900/95 text-white px-3 py-2 rounded-lg shadow-lg border border-gray-800">
        <div className="flex items-center gap-2 text-sm">
          <span className={`inline-block w-2 h-2 rounded-full ${dot}`}></span>
          <span className="truncate">{message}</span>
        </div>
      </div>
    </div>
  );
}

export default ToastBar;
