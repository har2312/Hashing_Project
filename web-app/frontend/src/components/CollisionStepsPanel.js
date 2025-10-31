import React, { useEffect, useRef } from 'react';

function CollisionStepsPanel({ steps, currentStep }) {
  const currentStepRef = useRef(null);

  // Auto-scroll to current step
  useEffect(() => {
    if (currentStepRef.current) {
      currentStepRef.current.scrollIntoView({
        behavior: 'smooth',
        block: 'center'
      });
    }
  }, [currentStep]);

  // Grouping: show steps in blocks of 5 (1-5, 6-10, ...), highlighting the current one
  const groupSize = 5;
  const total = steps ? steps.length : 0;
  const groupStart = total > 0 ? Math.floor(currentStep / groupSize) * groupSize : 0;
  const groupEndExclusive = Math.min(total, groupStart + groupSize);

  return (
    <div className="bg-white rounded-lg shadow-2xl p-2.5" style={{ height: 'calc(100vh - 240px)' }}>
      <h2 className="text-sm font-bold text-gray-800 mb-1.5 flex items-center gap-1.5">
        <span>🔍</span> Execution Steps
      </h2>

      {steps && steps.length > 0 ? (
        <div className="bg-gray-900 rounded-lg p-2 overflow-hidden">
          {steps.slice(groupStart, groupEndExclusive).map((step, index) => {
            const absoluteIndex = groupStart + index;
            const isCurrent = absoluteIndex === currentStep;
            return (
              <div
                key={absoluteIndex}
                ref={isCurrent ? currentStepRef : null}
                className={`mb-1.5 pb-1.5 border-b border-gray-700 last:border-0 transition-all duration-200 ${
                  isCurrent ? 'opacity-100 scale-[1.01]' : 'opacity-70'
                }`}
              >
                <div className="flex items-start gap-1.5">
                  <div
                    className={`flex-shrink-0 w-5 h-5 rounded-full flex items-center justify-center text-[9px] font-bold transition-all duration-200 ${
                      isCurrent ? 'bg-yellow-400 text-gray-900 ring-2 ring-yellow-200' : 'bg-gray-700 text-gray-300'
                    }`}
                  >
                    {absoluteIndex + 1}
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className={`text-[10px] font-mono break-words ${
                      isCurrent ? 'text-yellow-300 font-bold' : 'text-green-400'
                    }`}>
                      {step.text}
                    </div>
                    {step.vars && Object.keys(step.vars).length > 0 && (
                      <div className="mt-0.5 text-[9px] text-gray-500 font-mono">
                        {Object.entries(step.vars)
                          .slice(0, 4)
                          .map(([key, value]) => `${key}=${value}`)
                          .join(', ')}
                      </div>
                    )}
                  </div>
                </div>
              </div>
            );
          })}

          <div className="mt-1 flex justify-between items-center text-[9px] text-gray-400">
            <div>Showing {groupStart + 1}-{groupEndExclusive} of {total}</div>
            <div>{currentStep + 1} / {total} steps</div>
          </div>
        </div>
      ) : (
        <div className="text-center text-gray-500 py-4">
          <div className="text-2xl mb-1">⚙️</div>
          <p className="text-xs">Execution steps will appear here</p>
          <p className="text-[10px] mt-0.5">Perform operations to see details</p>
        </div>
      )}

      {steps && steps.length > 0 && (
        <div className="mt-2 p-1.5 bg-green-50 rounded-lg">
          <div className="text-[9px] text-gray-700">
            <div className="w-full bg-gray-200 rounded-full h-1 mb-1">
              <div
                className="bg-green-500 h-1 rounded-full transition-all duration-300"
                style={{ width: `${((currentStep + 1) / steps.length) * 100}%` }}
              />
            </div>
            <div className="text-[9px] text-gray-600 text-center">
              {currentStep + 1} / {steps.length} steps
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default CollisionStepsPanel;
