import React, { useState } from 'react';
import axios from 'axios';
import ControlPanel from './components/ControlPanel';
import HashTableVisualization from './components/HashTableVisualization';
import PseudocodePanel from './components/PseudocodePanel';
import CollisionStepsPanel from './components/CollisionStepsPanel';
import ToastBar from './components/ToastBar';
import './App.css';

// API base URL - automatically uses relative path in production
const API_URL = process.env.REACT_APP_API_URL || (
  process.env.NODE_ENV === 'production' 
    ? '/api'  // In production (Vercel), use relative path
    : 'https://hashing-api.vercel.app/api'  // In development, use localhost
);

function App() {
  const [tableId, setTableId] = useState(null);
  const [tableState, setTableState] = useState(null);
  const [pseudocode, setPseudocode] = useState([]);
  const [steps, setSteps] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);
  const [highlightedBucket, setHighlightedBucket] = useState(null);
  const [animationSpeed, setAnimationSpeed] = useState(800);
  const [statusMessage, setStatusMessage] = useState('Ready to start! Create a hash table to begin.');

  const getToastVariant = (msg) => {
    if (!msg) return 'info';
    const m = msg.toLowerCase();
    if (m.includes('error')) return 'error';
    if (m.includes('success') || m.includes('found')) return 'success';
    if (m.includes('table_full') || m.includes('not_found') || m.includes('please create')) return 'warn';
    return 'info';
  };

  const createTable = async (size, mode) => {
    try {
      const response = await axios.post(`${API_URL}/create`, { size, mode });
      setTableId(response.data.table_id);
      setTableState(response.data.state);
      setStatusMessage(response.data.message);
      setSteps([]);
      setPseudocode([]);
      setCurrentStep(0);
    } catch (error) {
      console.error('Error creating table:', error);
      setStatusMessage('Error creating table: ' + (error.response?.data?.error || error.message));
    }
  };

  const insertKey = async (key) => {
    if (!tableId) {
      setStatusMessage('Please create a table first!');
      return;
    }

    try {
      const response = await axios.post(`${API_URL}/${tableId}/insert`, { key });
      
      // Set pseudocode first
      setPseudocode(response.data.pseudocode || []);
      setSteps(response.data.steps || []);
      setCurrentStep(0);
      
      // Animate through steps if available
      if (response.data.steps && response.data.steps.length > 0) {
        animateSteps(response.data.steps, response.data.state, response.data.message);
      } else {
        // No animation, just update state
        setTableState(response.data.state);
        setStatusMessage(response.data.message);
      }
    } catch (error) {
      console.error('Error inserting key:', error);
      setStatusMessage('Error: ' + (error.response?.data?.error || error.message));
    }
  };

  const searchKey = async (key) => {
    if (!tableId) {
      setStatusMessage('Please create a table first!');
      return;
    }

    try {
      const response = await axios.post(`${API_URL}/${tableId}/search`, { key });
      
      // Set pseudocode and steps first
      setPseudocode(response.data.pseudocode || []);
      setSteps(response.data.steps || []);
      setCurrentStep(0);
      
      // Animate through steps if available
      if (response.data.steps && response.data.steps.length > 0) {
        animateSteps(response.data.steps, response.data.state, response.data.message);
      } else {
        // No animation, just update state
        setTableState(response.data.state);
        setStatusMessage(response.data.message);
        
        if (response.data.found) {
          setHighlightedBucket(response.data.index);
          setTimeout(() => setHighlightedBucket(null), 2000);
        }
      }
    } catch (error) {
      console.error('Error searching key:', error);
      setStatusMessage('Error: ' + (error.response?.data?.error || error.message));
    }
  };

  const deleteKey = async (key) => {
    if (!tableId) {
      setStatusMessage('Please create a table first!');
      return;
    }

    try {
      const response = await axios.post(`${API_URL}/${tableId}/delete`, { key });
      
      // Set pseudocode and steps first
      setPseudocode(response.data.pseudocode || []);
      setSteps(response.data.steps || []);
      setCurrentStep(0);
      
      // Animate through steps if available
      if (response.data.steps && response.data.steps.length > 0) {
        animateSteps(response.data.steps, response.data.state, response.data.message);
      } else {
        // No animation, just update state
        setTableState(response.data.state);
        setStatusMessage(response.data.message);
        
        if (response.data.success && response.data.index >= 0) {
          setHighlightedBucket(response.data.index);
          setTimeout(() => setHighlightedBucket(null), 2000);
        }
      }
    } catch (error) {
      console.error('Error deleting key:', error);
      setStatusMessage('Error: ' + (error.response?.data?.error || error.message));
    }
  };

  const resizeTable = async (newSize) => {
    if (!tableId) {
      setStatusMessage('Please create a table first!');
      return;
    }

    try {
      const response = await axios.post(`${API_URL}/${tableId}/resize`, { new_size: newSize });
      setTableState(response.data.state);
      setStatusMessage(response.data.message);
    } catch (error) {
      console.error('Error resizing table:', error);
      setStatusMessage('Error: ' + (error.response?.data?.error || error.message));
    }
  };

  const clearTable = async () => {
    if (!tableId) {
      setStatusMessage('Please create a table first!');
      return;
    }

    try {
      const response = await axios.post(`${API_URL}/${tableId}/clear`);
      setTableState(response.data.state);
      setStatusMessage(response.data.message);
      setSteps([]);
      setPseudocode([]);
    } catch (error) {
      console.error('Error clearing table:', error);
      setStatusMessage('Error: ' + (error.response?.data?.error || error.message));
    }
  };

  const animateSteps = (stepsList, finalState, finalMessage) => {
    // Reset to beginning
    setCurrentStep(-1);
    setHighlightedBucket(null);
    
    let stepIndex = 0;
    
    const animate = () => {
      if (stepIndex < stepsList.length) {
        // Update current step for pseudocode highlighting
        setCurrentStep(stepIndex);
        
        const step = stepsList[stepIndex];
        
        // Highlight bucket if specified
        if (step.highlight_bucket !== null && step.highlight_bucket !== undefined) {
          setHighlightedBucket(step.highlight_bucket);
        } else {
          setHighlightedBucket(null);
        }
        
        // Update status with current step text
        if (step.text) {
          setStatusMessage(step.text);
        }
        
        stepIndex++;
        setTimeout(animate, animationSpeed);
      } else {
        // Animation complete - update final state
        setTableState(finalState);
        setHighlightedBucket(null);
        setStatusMessage(finalMessage || 'Operation completed');
      }
    };
    
    // Start animation after a brief delay
    setTimeout(() => {
      animate();
    }, 100);
  };

  return (
    <div className="min-h-screen overflow-hidden bg-gradient-to-br from-indigo-600 via-purple-600 to-purple-800 p-2">
      <div className="max-w-[98vw] mx-auto">
        {/* Header - Ultra Compact */}
        <div className="text-center mb-1">
          <h1 className="text-3xl font-bold text-white drop-shadow-lg">
            🔐 Hash Table Simulator
          </h1>
        </div>

        {/* Control Panel */}
        <ControlPanel
          onCreateTable={createTable}
          onInsertKey={insertKey}
          onSearchKey={searchKey}
          onDeleteKey={deleteKey}
          onResizeTable={resizeTable}
          onClearTable={clearTable}
          tableState={tableState}
          animationSpeed={animationSpeed}
          setAnimationSpeed={setAnimationSpeed}
        />

  {/* Toast under Control Panel */}
  <ToastBar message={statusMessage} variant={getToastVariant(statusMessage)} />

        {/* Main Content Area - Three columns: table | pseudocode | steps */}
  <div className="grid grid-cols-1 lg:grid-cols-3 gap-2 mt-2 overflow-hidden">
          <HashTableVisualization
            tableState={tableState}
            highlightedBucket={highlightedBucket}
          />
          <PseudocodePanel
            pseudocode={pseudocode}
            currentStep={currentStep}
            steps={steps}
          />
          <CollisionStepsPanel
            steps={steps}
            currentStep={currentStep}
            compact={true}
          />
        </div>

        {/* Removed bottom status bar in favor of toast */}
      </div>
    </div>
  );
}

export default App;
