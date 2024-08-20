/** @jsxImportSource @emotion/react */
import React from 'react'

import { BrowserRouter, Route, Routes, Link } from 'react-router-dom'
import { PhraseInput, MenuBoard } from './componetns/index'
import './App.css'

function App() {
    return (
        <div>
            <BrowserRouter>
                <div className="App">
                    <Link to="/" target="_blank">
                        Home
                    </Link>
                    <br />
                    <Link to="/page1" target="_blank">
                        Title Input Page
                    </Link>
                    <br />
                    <Routes>
                        <Route exact path="/" element={<MenuBoard />}></Route>
                        <Route path="/page1" element={<PhraseInput />}></Route>
                    </Routes>
                </div>
            </BrowserRouter>
        </div>
    )
}

export default App

