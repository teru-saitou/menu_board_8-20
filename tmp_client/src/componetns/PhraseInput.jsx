/* eslint-disable react/no-unknown-property */
import React from 'react'
/** @jsxImportSource @emotion/react */
import { css } from '@emotion/react'
import { useState } from 'react'
import axios from 'axios'

const PhraseInput = () => {
    const [inputData, setInputData] = useState('')

    const url = 'http://127.0.0.1:8000/chatch_phrase'

    // useEffect(() => {
    const handleSubmit = async e => {
        console.log('in function')
        console.log(inputData)
        e.preventDefault()
        try {
            const res = await axios.post(url, { data: inputData })
            if (res.status === axios.HttpStatusCode.Ok) {
                setInputData(res.data.name)
                console.log('res data')
                console.log(res.data.name)
                console.log('inputData')
                console.log(inputData)
            }
        } catch (error) {
            console.error('データの登録に失敗しました。', error)
            console.log('case_failed')
            console.log(inputData)
        }
    }

    const container = css`
        background-color: #eddee8;
        padding: 10px;
    `

    const innerContainer = css`
        background-color: #c3ebdb;
        text-align: center;
        padding: 5rem;
    `

    const catchPhrase = css`
        height: 100%;
        padding: 2rem;
        font-size: 10px;
        background-color: #f89573;
        white-space: pre-wrap;
        border: solid 5px #021d46;
        border-radius: 10px;
    `

    const registerButton = css`
        /* padding-top: 10px; */
        display: flex;
        justify-content: space-evenly;
        align-items: center;
        text-align: center;
        text-decoration: none;
        width: 150px;
        margin-left: auto;
        padding: 1rem 2rem 1rem 2rem;
        font-weight: bold;
        background: #27acd9;
        color: #fff;
        border-radius: 100vh;
        position: relative;
        transition: 0.5s;
        &::before {
            content: '';
            white-space: pre-wrap;
            width: 7px;
            height: 7px;
            border-top: 2px solid #fff;
            border-right: 2px solid #fff;
            transform: rotate(45deg);
        }
        &:hover {
            background: #44c6f2;
            color: #fff;
        }
    `

    return (
        <div className="conteiner" css={container}>
            <div className="wrapper" css={innerContainer}>
                <h1>Catchpharase Input Page</h1>
                <form onSubmit={handleSubmit} css={catchPhrase}>
                    <textarea
                        type="text"
                        value={inputData}
                        onChange={e => setInputData(e.target.value)}
                        placeholder="キャッチコピーを入力して下さい"
                        rows="4"
                        cols="50"
                    />
                    <button type="submit" css={registerButton}>
                        登録する
                    </button>
                </form>
            </div>
        </div>
    )
}

export default PhraseInput
