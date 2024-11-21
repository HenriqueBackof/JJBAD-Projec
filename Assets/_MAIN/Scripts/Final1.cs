
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using TMPro;

public class Final1 : MonoBehaviour
{
    [SerializeField] private string menuDeEntrada;

    [SerializeField] private GameObject botaoReiniciar;

    public void reiniciarJogo() {
        SceneManager.LoadScene(menuDeEntrada);
        VariavelGlobal.instance.resetScore();
        VariavelGlobal.instance.pararMusica();
    }
}   
