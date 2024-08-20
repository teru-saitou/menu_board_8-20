/* eslint-disable react/no-unknown-property */
/** @jsxImportSource @emotion/react */
import { css } from "@emotion/react";
import { useState, useEffect } from "react";
import React from "react";
import axios from "axios";
import { Link as Scroll } from "react-scroll";

/**
 * @return {number} スマレジデベロッパーズから商品名、価格、商品画像を取得する
 */
function MenuBoard() {
  const [dataList, setDataList] = useState([]);
  const [imageList, setImageList] = useState([]);
  const [phrase, setPhrase] = useState([]);
  const failure_message = "の取得に失敗しました";

  const axiosInstance = axios.create({
    baseURL: process.env.REACT_APP_API_BASE_URL
  });

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await axiosInstance.get("/chatch_phrase");
        if (res.status === axios.HttpStatusCode.Ok) {
          setPhrase(res.data);
          console.log(res);
        } else {
          console.error("キャッチコピー", failure_message);
        }
      } catch (error) {
        console.error("キャッチコピー", failure_message, error);
      }
    };
    fetchData();
  }, []);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await  axiosInstance.get("/products");
        if (res.status === axios.HttpStatusCode.Ok) {
          setDataList(res.data);
          console.log(res.data);
        } else {
          console.error("商品データ", failure_message);
        }
      } catch (error) {
        console.error("商品データ", failure_message, error);
      }
    };
    fetchData();
  }, []);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await axiosInstance.get("/images");
        if (res.status === axios.HttpStatusCode.Ok) {
          setImageList(res.data);
          console.log(res.data);
        } else {
          console.error("画像データ", failure_message);
        }
      } catch (error) {
        console.error("画像データ", failure_message, error);
      }
    };
    fetchData();
  }, []);

  const container = css`
    background-color: #e9d5e1;
    padding: 30px 200px;
    font-family: "ヒラギノ角ゴ ProN W3", HiraKakuProN-W3, 游ゴシック,
      "Yu Gothic", メイリオ, Meiryo, Verdana, Helvetica, Arial, sans-serif;
  `;

  const innerContainer = css`
    background-color: #d3f5e8;
    text-align: center;
    padding: 20px;
    border: solid 10px #1a2638;
    border-radius: 10px;
  `;

  const menuBoard = css`
    background-color: #c4e9fa;
    font-size: 50px;
    text-align: center;
    padding-top: 10px;
    padding-bottom: 10px;
  `;

  const catchPhrase = css`
    padding-top: 10px;
    padding-bottom: 10px;
    font-size: 30px;
    background-color: #f0d9c2;
    white-space: pre-wrap;
  `;

  const menuWrapper = css`
    background-color: #fff;
    padding: 20px;
    display: flex;
    justify-content: center;
    height: 500px;
    overflow: scroll;
  `;

  const errorMessage = css`
    white-space: pre-wrap;
  `;

  const menuCategory = css`
    background-color: #f6f3e2;
    padding-bottom: 20px;
  `;

  const menuContents = css`
    color: #2e313d;
    font-size: 30px;
    padding: 100px 10px 103px 10px;
  `;

  const navConteiner = css`
    display: -webkit-flex;
    display: flex;
    -webkit-justify-content: space-around;
    justify-content: space-around;
    padding: 20px 100px;
  `;

  const scrol = css`
    border: solid 3px #13294a;
    border-radius: 10px;
    padding: 5px;
  `;

  const yen = "円";
  const dataNotRetrieved = `Data couldn't be obtained.`;
  const title = `Menu Board`;

  console.log("contents of datalist");
  console.log(dataList);
  console.log("contents of imagelist");
  console.log(imageList);
  console.log("contents of phrase");
  console.log(phrase);
  //ロジックを圧縮できる方法は？
  return (
    <div>
      <div className="container" css={container}>
        <div className="navcontainer" css={navConteiner}>
          {["menuBottom", "menuTop"].map((target, index) => (
            <div css={scrol} key={target}>
              <Scroll
                to={target}
                smooth={true}
                duration={25000}
                containerId="overFlowScrollArea"
              >
                {index === 0 ? "全メニューを表示する" : "メニューの先頭へ戻る"}
              </Scroll>
            </div>
          ))}
          {/* <div css={scrol}>
                        <Scroll to="menuBottom" smooth={true} duration={25000} containerId="overFlowScrollArea">
                            全メニューを表示する
                        </Scroll>
                    </div>
                    <div css={scrol}>
                        <Scroll to="menuTop" smooth={true} duration={25000} containerId="overFlowScrollArea">
                            メニューの先頭へ戻る
                        </Scroll>
                    </div> */}
        </div>
        <div className="innerContainer" css={innerContainer}>
          <div className="title" css={menuBoard}>
            {title}
          </div>
          <div className="catchPhrase" css={catchPhrase}>
            {phrase}
          </div>
          <div className="catchPhrase"></div>
          <div
            className="menuWrapper"
            css={menuWrapper}
            id="overFlowScrollArea"
          >
            <div className="menuName" css={menuCategory} id="menuTop">
              {Array.isArray(dataList) ? (
                dataList.map((item) => (
                  <div
                    key={item.productCode}
                    className="menuName"
                    css={menuContents}
                  >
                    {item.productName}
                  </div>
                ))
              ) : (
                <p css={errorMessage}>{dataNotRetrieved}</p>
              )}
              <div id="menuBottom"></div>
            </div>

            <div>
              {imageList.map((image) => (
                <div key={image.productId}>
                  <img
                    src={image.url}
                    alt="menuImage"
                    width={242}
                    height={242}
                  />
                </div>
              ))}
            </div>

            <div className="menuPeice" css={menuCategory}>
              {Array.isArray(dataList) ? (
                dataList.map((item) => (
                  <div
                    key={item.productId}
                    className="menuPrice"
                    css={menuContents}
                  >
                    {item.price}
                    {yen}
                  </div>
                ))
              ) : (
                <p css={errorMessage}>{dataNotRetrieved}</p>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default MenuBoard;
