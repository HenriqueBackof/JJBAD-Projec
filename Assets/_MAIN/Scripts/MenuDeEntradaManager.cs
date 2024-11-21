using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class MenuDeEntradaManager : MonoBehaviour
{
    [SerializeField] private string nomeDoLevelDoJogo;
    [SerializeField] private GameObject painelMenuDeEntrada;
    [SerializeField] private GameObject painelOptions;
    [SerializeField] private AudioSource selecaoBotao;
     
     public void newGame() {
        SceneManager.LoadScene(nomeDoLevelDoJogo);
        VariavelGlobal.instance.tocarAudioClip();
        selecaoBotao.Play();
     }

     public void options() {
        painelMenuDeEntrada.SetActive(false);
        painelOptions.SetActive(true);
        selecaoBotao.Play();
     }

     public void backToMenu() {
        painelOptions.SetActive(false);
        painelMenuDeEntrada.SetActive(true);
        selecaoBotao.Play();
     }
}
