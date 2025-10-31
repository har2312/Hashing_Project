import React, { useEffect, useRef } from 'react';

function PseudocodePanel({ pseudocode, currentStep, steps }) {
  const highlightedLineRef = useRef(null);

  const getHighlightedLine = () => {
    if (steps && currentStep >= 0 && steps[currentStep]) {
      return steps[currentStep].line;
    }
    return -1;
  };

  const highlightedLine = getHighlightedLine();

  // Auto-scroll to highlighted line
  useEffect(() => {
    if (highlightedLineRef.current) {
      highlightedLineRef.current.scrollIntoView({
        behavior: 'smooth',
        block: 'center'
      });
    }
  }, [highlightedLine]);

  const getCurrentVariables = () => {
    if (steps && currentStep >= 0 && steps[currentStep]) {
      return steps[currentStep].vars || {};
    }
    return {};
  };

  const variables = getCurrentVariables();

  return (
    <div className="bg-white rounded-lg shadow-2xl p-2.5" style={{ height: 'calc(100vh - 240px)' }}>
      <h2 className="text-sm font-bold text-gray-800 mb-1.5 flex items-center gap-1.5">
        <span>📝</span> Pseudocode
      </h2>

      {pseudocode && pseudocode.length > 0 ? (
        <>
          {/* Pseudocode Display - No scroll; compressed */}
          <div className="bg-gray-900 rounded-lg p-2 mb-2 font-mono text-[9px] leading-tight overflow-hidden">
            {pseudocode.map((line, index) => {
              // Calculate indentation level from leading spaces
              const indent = line.match(/^\s*/)[0].length;
              const indentLevel = Math.floor(indent / 2);
              
              return (
                <div
                  key={index}
                  ref={index + 1 === highlightedLine ? highlightedLineRef : null}
                  className={`py-0.5 px-1.5 rounded transition-all duration-300 ${
                    index + 1 === highlightedLine
                      ? 'bg-yellow-400 text-gray-900 font-bold scale-105 shadow-lg'
                      : 'text-green-400'
                  }`}
                  style={{ 
                    paddingLeft: `${6 + indentLevel * 12}px`,
                    whiteSpace: 'pre'
                  }}
                >
                  <span className="text-gray-500 mr-1.5 inline-block w-4 text-[8px]">{index + 1}</span>
                  <span>{line.trim()}</span>
                </div>
              );
            })}
          </div>

          {/* Variables Display - Compact */}
          {Object.keys(variables).length > 0 && (
            <div className="bg-blue-50 rounded-lg p-2 mb-1.5">
              <div className="text-[9px] font-semibold text-gray-700 mb-0.5">
                Variables:
              </div>
              <div className="flex flex-wrap gap-1.5">
                {Object.entries(variables).map(([key, value]) => (
                  <div key={key} className="inline-flex items-center gap-0.5 text-[9px] bg-white px-1.5 py-0.5 rounded">
                    <span className="font-mono font-bold text-blue-600">{key}:</span>
                    <span className="font-mono text-gray-800">
                      {typeof value === 'string' ? `"${value}"` : value}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Step Info - Compact */}
          {steps && steps.length > 0 && (
            <div className="text-[9px] text-gray-600 text-center py-0.5">
              Step {currentStep + 1} / {steps.length}
            </div>
          )}
        </>
      ) : (
        <div className="text-center text-gray-500 py-4">
          <div className="text-2xl mb-1">📖</div>
          <p className="text-xs">Pseudocode will appear here</p>
          <p className="text-[10px] mt-0.5">Insert a key to see execution</p>
        </div>
      )}

      {/* Instructions - Ultra Compact */}
      <div className="mt-1.5 p-1.5 bg-purple-50 rounded-lg">
        <div className="text-[9px] text-gray-600 space-y-0">
          <div>• <span className="font-semibold">Yellow</span> = Current line</div>
          <div>• <span className="font-semibold">Indentation</span> = Loop depth</div>
        </div>
      </div>
    </div>
  );
}

export default PseudocodePanel;
