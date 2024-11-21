
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using TMPro;

public class Final2 : MonoBehaviour
{
    [SerializeField] private string menuDeEntrada;
    [SerializeField] private GameObject FinalBom;
    [SerializeField] private GameObject FinalRuim;
    [SerializeField] private GameObject botaoReiniciar;

     void Start() {
        MostrarFinal();
    } 

    public void MostrarFinal() {
        int pontuacao = VariavelGlobal.instance.getScore();
        if (pontuacao >= 30) {
            FinalBom.SetActive(true);
        } else {
            FinalRuim.SetActive(true);
        }
    }

    public void reiniciarJogo() {
        SceneManager.LoadScene(menuDeEntrada);
        VariavelGlobal.instance.resetScore();
        VariavelGlobal.instance.pararMusica();
    }

}   
