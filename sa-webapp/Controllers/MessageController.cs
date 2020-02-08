using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Mvc;
using sa_webapp.Models;
using sa_webapp.Services;

namespace sa_webapp.Controllers
{
    [Produces("application/json")]
    [Route("sentiment/[controller]")]
    [ApiController]
    [EnableCors("ReactPolicy")]
    public class MessageController : Controller
    {
        private readonly MessageService msgService;
        public MessageController(MessageService msgService)
        {
            this.msgService = msgService;
        }

        public Message Get()
        {
            Console.WriteLine("asdf");
            return new Message();
        }

        [HttpPost]
        public async Task<IActionResult> Post([FromBody] Message msg)
        {
            return CreatedAtAction("Get", new { id = msg.answer }, msgService.ask(msg));
            // Console.WriteLine("In Post Method");
            // return CreatedAtAction("Get", new Message());
        }
        
    }
}